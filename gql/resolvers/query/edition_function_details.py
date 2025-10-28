from typing import List
from gql.types import EditionFunctionDetailsType
from gql.config import edition_function_details as PATH
from gql.services.data_service import DataService
from gql.resolvers.transformers import transform_to_edition_function_details


# Create a singleton service instance
edition_function_service = DataService(
    path=PATH,
    entity_type=EditionFunctionDetailsType,
    transform_func=transform_to_edition_function_details
)
# This gets called for each GraphQL query
def get_edition_function_details() -> List[EditionFunctionDetailsType]:
    """Resolver that returns all edition function details."""
    return edition_function_service.get_data()