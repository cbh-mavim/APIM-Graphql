from typing import List
from gql.types import ManagerUserLoginDetailsType
from gql.config import manager_user_login_details as PATH
from gql.services.data_service import DataService
from gql.resolvers.transformers import transform_to_manager_user_login_details
# Create a singleton service instance
users_service = DataService(path=PATH,
                            entity_type=ManagerUserLoginDetailsType,
                            transform_func=transform_to_manager_user_login_details)


# This gets called for each GraphQL query
def get_manager_user_login_details() -> List[ManagerUserLoginDetailsType]:
    """Resolver that returns all users."""
    return users_service.get_data()
    