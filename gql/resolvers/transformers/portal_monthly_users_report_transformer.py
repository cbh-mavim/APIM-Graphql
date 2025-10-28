from typing import Any, Dict
from gql.types import PortalMonthlyUserReportType
from gql.utils.datetime import parse_mavim_date


def transform_to_portal_monthly_users_report(
        row: Dict[str, Any]) -> PortalMonthlyUserReportType:
    """Transform a data row to a PortalMonthlyUserReportType."""
    return PortalMonthlyUserReportType(
        report_id=row['report_id'],
        portal_id=row['portal_id'],
        portal_name=row['portal_name'],
        portal_sql_database=row['portal_sql_database'],
        users_count=row['users_count'],
        month=row['month'],
        year=row['year'],
        created_date=parse_mavim_date(row['created_date']))
