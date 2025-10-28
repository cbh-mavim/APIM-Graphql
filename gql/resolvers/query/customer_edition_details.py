from typing import List
from gql.types import CustomerEditionDetailsType
from gql.config import customer_edition_details as PATH
from gql.services.data_service import DataService
from gql.resolvers.transformers import transform_to_customer_edition_details


# Create a singleton service instance
customer_edition_service = DataService(
    path=PATH,
    entity_type=CustomerEditionDetailsType,
    transform_func=transform_to_customer_edition_details
)

# This gets called for each GraphQL query
def get_customer_edition_details() -> List[CustomerEditionDetailsType]:
    """Resolver that returns all customer edition details."""
    return customer_edition_service.get_data()