import uvicorn
from fastapi import FastAPI,Request,Depends
from strawberry.fastapi import GraphQLRouter
from gql.schemas import schema
from gql.context import get_context

# Create FastAPI application
app = FastAPI(title="Azure GraphQL Platform Processor")

# Add GraphQL endpoint to FastAPI
graphql_app = GraphQLRouter(schema,context_getter=get_context,graphql_ide="graphiql")
app.include_router(graphql_app, prefix="/graphql")

# Add a root endpoint that redirects to GraphQL playground
@app.get("/")
async def root():
    return {"message": "Welcome to Azure GraphQL Platform Processor", "graphql_endpoint": "/graphql"}

def main():
    """Run the GraphQL server locally"""
    print("Starting GraphQL server...")
    uvicorn.run('main:app', host='0.0.0.0', port=8000)

if __name__ == "__main__":
    main()
    