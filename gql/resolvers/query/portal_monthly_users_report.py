from typing import List
from gql.types import PortalMonthlyUserReportType
from gql.config import portal_monthly_users_report as PATH
from gql.services.data_service import DataService
from gql.resolvers.transformers import transform_to_portal_monthly_users_report

# Create a singleton service instance
portal_monthly_users_report_service = DataService(
    path=PATH,
    entity_type=PortalMonthlyUserReportType,
    transform_func=transform_to_portal_monthly_users_report
)
# This gets called for each GraphQL query
def get_portal_monthly_users_report() -> List[PortalMonthlyUserReportType]:
    """Resolver that returns all portal monthly user reports."""
    return portal_monthly_users_report_service.get_data()