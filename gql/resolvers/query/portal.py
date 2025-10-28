from typing import List
from gql.types import PortalType
from gql.config import portal as PATH
from gql.services.data_service import DataService
from gql.resolvers.transformers import transform_to_portal

# Create a singleton service instance
portal_service = DataService(path=PATH,
                             entity_type=PortalType,
                             transform_func=transform_to_portal)


# This gets called for each GraphQL query
def get_portal() -> List[PortalType]:
    """Resolver that returns all portals."""
    return portal_service.get_data()
