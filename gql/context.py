from fastapi import Request,Depends
from typing import Optional
from auth import verify_token, User


#Function to detect the GraphiQL Request
def is_graphql_request(request: Request)->bool:
    return (
        request.method == "GET"
        and "text/html" in request.headers.get("accept", "")
        and not request.headers.get("authorization")
    )

#Authentication check
async def conditional_verify_token(request:Request)->Optional[User]:
    if is_graphql_request(request):
        return None
    return await verify_token(request)

#Context Builder
async def get_context(request: Request, user: Optional[User] = Depends(conditional_verify_token)):
    return{
        "request" : request,
        "user" : user
    }