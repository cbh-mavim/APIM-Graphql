from typing import List
from gql.types import LicenseCustomerProductType
from gql.config import license_customer_product as PATH
from gql.services.data_service import DataService
from gql.resolvers.transformers import transform_to_license_customer_product

# Create a singleton service instance
license_customer_product_service = DataService(
    path=PATH,
    entity_type=LicenseCustomerProductType,
    transform_func=transform_to_license_customer_product
)

# This gets called for each GraphQL query
def get_license_customer_product() -> List[LicenseCustomerProductType]:
    """Resolver that returns all license customer products."""
    return license_customer_product_service.get_data()