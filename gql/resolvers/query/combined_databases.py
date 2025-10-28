from typing import List
from gql.services.data_service import DataService
from gql.types import CombinedDatabasesType
from gql.config import combined_databases as PATH
from gql.resolvers.transformers import transform_to_combined_databases

# Create a singleton service instance
company_service = DataService(path=PATH,
                              entity_type=CombinedDatabasesType,
                              transform_func=transform_to_combined_databases)


# This gets called for each GraphQL query
def get_combined_databases() -> List[CombinedDatabasesType]:
    return company_service.get_data()
