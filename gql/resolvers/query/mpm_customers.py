from typing import List
from gql.types import MpmCustomerType
from gql.config import mpm_customers as PATH
from gql.services.data_service import DataService
from gql.resolvers.transformers import transform_to_mpm_customer

# Create a singleton service instance
mpm_customer_service = DataService(
    path=PATH,
    entity_type=MpmCustomerType,
    transform_func=transform_to_mpm_customer
)
# This gets called for each GraphQL query
def get_mpm_customers() -> List[MpmCustomerType]:
    """Resolver that returns all MPM customers."""
    return mpm_customer_service.get_data()