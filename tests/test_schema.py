"""
Tests for the GraphQL schema.
"""
import pytest
from strawberry.test import BaseGraphQLTestCase
from gql import schema
from strawberry.asgi import GraphQL

class TestGraphQLSchema(BaseGraphQLTestCase):
    """Test case for the GraphQL schema."""
    
    def get_client(self):
        """Return the GraphQL client for testing."""
        return GraphQL(schema)
    
    async def test_schema_query(self):
        """Test that the schema can be queried."""
        # This is a simple test to check if the schema is valid
        # and can be queried with an introspection query
        query = """
        {
          __schema {
            queryType {
              name
            }
          }
        }
        """
        
        response = await self.client.execute(query)
        
        # Check that the response is successful
        assert "errors" not in response
        assert "data" in response
        assert "__schema" in response["data"]
        assert "queryType" in response["data"]["__schema"]
        assert "name" in response["data"]["__schema"]["queryType"]
