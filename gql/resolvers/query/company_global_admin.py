from typing import List
from gql.services.data_service import DataService
from gql.types import CompanyGlobalAdminType
from gql.config import company_global_admins as PATH
from gql.resolvers.transformers import transform_to_company_global_admin

# Create a singleton service instance
company_global_admin_service = DataService(path=PATH,
                              entity_type=CompanyGlobalAdminType,
                              transform_func=transform_to_company_global_admin)


# This gets called for each GraphQL query
def get_company_global_admin() -> List[CompanyGlobalAdminType]:
    return company_global_admin_service.get_data()


