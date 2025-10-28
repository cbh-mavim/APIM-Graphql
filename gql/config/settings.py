from dataclasses import dataclass, field
import os
from dotenv import load_dotenv

# Load .env file from the root directory
load_dotenv()

@dataclass
class AuthSettings:
    # Load required settings from environment. The app will fail to start if they are missing.
    tenant_id: str = os.getenv("TENANT_ID")
    client_id: str = os.getenv("CLIENT_ID")
    issuer: str = field(init=False)
    openid_config_url: str = field(init=False)
    algorithms: list[str] = field(default_factory=lambda: ["RS256"])

    def __post_init__(self):
        if not self.tenant_id or not self.client_id:
            raise ValueError("Error: TENANT_ID and CLIENT_ID must be set in the environment.")
        
        self.issuer = f"https://login.microsoftonline.com/{self.tenant_id}/v2.0"
        self.openid_config_url = f"{self.issuer}/.well-known/openid-configuration"

# Create a single, reusable instance of the settings
auth_settings = AuthSettings()