from typing import List
from gql.types import UserMavimManagerLicenseType
from gql.config import users as PATH
from gql.services.data_service import DataService
from gql.resolvers.transformers import transform_to_user_mavim_manager_license
# Create a singleton service instance
users_service = DataService(path=PATH,
                            entity_type=UserMavimManagerLicenseType,
                            transform_func=transform_to_user_mavim_manager_license)


# This gets called for each GraphQL query
def get_users_mavim_manager() -> List[UserMavimManagerLicenseType]:
    """Resolver that returns all users."""
    return users_service.get_data()
