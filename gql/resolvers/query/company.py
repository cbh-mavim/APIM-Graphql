from typing import List
from gql.types import CompanyType
from gql.config import company as COMPANY_PATH
from gql.services.data_service import DataService
from gql.resolvers.transformers import transform_to_company

# Create a singleton service instance
company_service = DataService(path=COMPANY_PATH,
                              entity_type=CompanyType,
                              transform_func=transform_to_company)


# This gets called for each GraphQL query
def get_companies() -> List[CompanyType]:
    """Resolver that returns all companies."""
    return company_service.get_data()
