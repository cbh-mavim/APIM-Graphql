import logging
from fastapi import Request, HTTPException
from jose import jwt, JWTError
import httpx  # type: ignore
from typing import Optional, List
from time import time
from gql.config.settings import auth_settings

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("Auth")

# Fetching the values from the centralized settings object
ISSUER = auth_settings.issuer
OPENID_CONFIG_URL = auth_settings.openid_config_url
ALGORITHMS = auth_settings.algorithms

# Authentication Header for Power BI, built from settings
AUTH_CHALLENGE_HEADER = {
    "WWW-Authenticate": f'Bearer authorization_uri="https://login.microsoftonline.com/{auth_settings.tenant_id}", resource_id="{auth_settings.client_id}"'
}

# User Class - Using it because we need to check the roles and scopes for Authorization
class User:
    def __init__(self, id: str, name: Optional[str] = None, roles: Optional[List[str]] = None, scp: Optional[str] = None):
        self.id = id
        self.name = name
        self.roles = roles or []
        self.scp = scp

# JWKS Caching Setup - Using it because so we can use the cached JWT itself if the Token is not yet Expired
jwks_cache = {
    "keys": None,
    "expiry": 0
}
CACHE_LIFETIME_SECONDS = 3600

# JWKS Fetching Function - Fetching the JWKS from Azure or Returning the Cached Keys if they are not expired yet.
async def get_jwks():
    global jwks_cache
    current_time = time()

    if jwks_cache["keys"] and jwks_cache["expiry"] > current_time:
        logger.info("[Auth] Using the cached JWKS")
        return jwks_cache["keys"]
    
    logger.info("[Auth] Fetching new JWKS from: %s", OPENID_CONFIG_URL)
    async with httpx.AsyncClient() as client:
        try:
            oidc_res = await client.get(OPENID_CONFIG_URL)
            oidc_res.raise_for_status()
            oidc_config = oidc_res.json()
            jwks_uri = oidc_config["jwks_uri"]

            jwks_res = await client.get(jwks_uri)
            jwks_res.raise_for_status()
            jwks = jwks_res.json()

            jwks_cache["keys"] = jwks
            jwks_cache["expiry"] = current_time + CACHE_LIFETIME_SECONDS
            logger.info("[Auth] Successfully fetched and cached new JWKS.")
            return jwks
        except httpx.HTTPError as e:
            logger.error("[Auth][Error] Failed to fetch OpenID Config or JWKS: %s", e)
            raise HTTPException(status_code=500, detail="Could not fetch the security keys for authentication.")
            

# Token Verification Function - The Function which verifies the token whether it has the required aud iss and also checks the signature
async def verify_token(request: Request) -> User:
    auth_header = request.headers.get("Authorization")
    if not auth_header:
        logger.warning("[Auth][WARN] Missing Authorization header. Sending 401 challenge.")
        raise HTTPException(status_code=401, detail="Authorization header is missing", headers=AUTH_CHALLENGE_HEADER)
    
    try:
        scheme, token = auth_header.split()
        if scheme.lower() != "bearer":
            raise HTTPException(status_code=401, detail="Invalid authentication scheme. Must be 'Bearer'.", headers=AUTH_CHALLENGE_HEADER)
    except ValueError:
        raise HTTPException(status_code=401, detail="Invalid Authorization header format.", headers=AUTH_CHALLENGE_HEADER)
    
    try:
        jwks = await get_jwks()
        unverified_header = jwt.get_unverified_header(token)
        rsa_key = next((key for key in jwks["keys"] if key["kid"] == unverified_header.get("kid")), None)

        if not rsa_key:
            logger.error("[Auth] [ERROR] No matching key ID (kid) found in JWKS.")
            raise HTTPException(status_code=401, detail="Unable to find a matching key to verify the token.", headers=AUTH_CHALLENGE_HEADER)
        
        payload = jwt.decode(
            token,
            rsa_key,
            algorithms=ALGORITHMS,
            audience=auth_settings.client_id,  # <-- CRITICAL FIX HERE
            issuer=ISSUER
        )
    
        user = User(
            id=payload.get("oid"),
            name=payload.get("name"),
            roles=payload.get("roles"),
            scp=payload.get("scp")
        )

        logger.info("[Auth] Token successfully verified for User ID: %s", user.id)
        return user
    
    except JWTError as e:
        logger.error("[Auth][ERROR] Token Validation failed: %s", e)
        raise HTTPException(status_code=401, detail=f"Invalid token: {e}", headers=AUTH_CHALLENGE_HEADER)
    except Exception as e:
        logger.error("[Auth][ERROR] An unexpected error occurred during token verification: %s", e)
        raise HTTPException(status_code=500, detail="An error occurred during token verification.")