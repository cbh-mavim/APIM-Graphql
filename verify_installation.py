#!/usr/bin/env python
"""
Verify that the azure-graphql-platform-processor package is installed correctly.

This script attempts to import key components from the package and
prints a success message if all imports work correctly.
"""

def verify_installation():
    """Verify that the package is installed correctly."""
    try:
        # Import the schema
        from gql import schema
        print("✓ Successfully imported schema")
        
        # Import GraphQL components
        from strawberry.asgi import GraphQL
        app = GraphQL(schema)
        print("✓ Successfully created GraphQL application")
        
        # Try to access some components from the package
        from gql.schemas import query
        print("✓ Successfully imported query module")
        
        # All imports successful
        print("\n✅ The azure-graphql-platform-processor package is installed correctly!")
        print("You can now use it in your projects.")
        
    except ImportError as e:
        print(f"❌ Error: {e}")
        print("\nThe package may not be installed correctly.")
        print("Try reinstalling with: pip install -e .")
        return False
    
    return True

if __name__ == "__main__":
    verify_installation()
