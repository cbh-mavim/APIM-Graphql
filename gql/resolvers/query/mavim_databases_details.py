from typing import List
from gql.types import MavimDatabaseType
from gql.config import mavim_databases_details as PATH
from gql.services.data_service import DataService
from gql.resolvers.transformers import transform_to_mavim_database_details

# Create a singleton service instance
mavim_database_service = DataService(
    path=PATH,
    entity_type=MavimDatabaseType,
    transform_func=transform_to_mavim_database_details
)

# This gets called for each GraphQL query
def get_mavim_databases_details() -> List[MavimDatabaseType]:
    """Resolver that returns all Mavim database details."""
    return mavim_database_service.get_data()