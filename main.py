import uvicorn
from datetime import datetime
from fastapi import FastAPI
from strawberry.asgi import GraphQL
from gql.schemas import schema

# Create FastAPI application
app = FastAPI(title="Azure GraphQL Platform Processor")

# Add GraphQL endpoint to FastAPI
graphql_app = GraphQL(schema)
app.add_route("/graphql", graphql_app)
app.add_websocket_route("/graphql", graphql_app)


# Add a root endpoint that redirects to GraphQL playground
@app.get("/")
async def root():
    return {"message": "Welcome to Azure GraphQL Platform Processor", "graphql_endpoint": "/graphql"}

# Add health check endpoint
@app.get("/healthcheck")
async def healthcheck():
    """Health check endpoint for monitoring and load balancers"""
    return {
        "status": "healthy",
        "service": "Azure GraphQL Platform Processor",
        "version": "1.0.0",
        "timestamp": datetime.utcnow().isoformat() + "Z"
    }

# Alternative health check endpoints (common variations)
@app.get("/health")
async def health():
    """Alternative health check endpoint"""
    return await healthcheck()

@app.get("/status")
async def status():
    """Status endpoint"""
    return await healthcheck()

def main():
    """Run the GraphQL server locally"""
    print("Starting GraphQL server...")
    uvicorn.run('main:app', host='0.0.0.0', port=8000)

if __name__ == "__main__":
    main()
    