
from typing import List
from gql.types import CustomerAddonDetailsType
from gql.config import customer_addon_details as PATH
from gql.services.data_service import DataService
from gql.resolvers.transformers import transform_to_customer_addons_details

# Create a singleton service instance
customer_addon_service = DataService(
    path=PATH,
    entity_type=CustomerAddonDetailsType,
    transform_func=transform_to_customer_addons_details
)

# This gets called for each GraphQL query
def get_customer_addons_details() -> List[CustomerAddonDetailsType]:
    """Resolver that returns all customer addon details."""
    return customer_addon_service.get_data()