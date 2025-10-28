from typing import List
from gql.types import CombinedUsersType
from gql.config import combined_users as PATH
from gql.services.data_service import DataService
from gql.resolvers.transformers import transform_to_combined_users

# Create a singleton service instance
company_service = DataService(path=PATH,
                              entity_type=CombinedUsersType,
                              transform_func=transform_to_combined_users)


# This gets called for each GraphQL query
def get_combined_users() -> List[CombinedUsersType]:
    return company_service.get_data()
