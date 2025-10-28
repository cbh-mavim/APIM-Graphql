from datetime import date
import strawberry
from typing import Optional

from gql.utils.datetime import DateTimeISO
    
@strawberry.type
class PortalMonthlyUserReportType:
    report_id: int
    portal_id: int
    portal_name: str
    portal_sql_database: str
    users_count: Optional[int]
    month: str
    year: str
    created_date: Optional[DateTimeISO]

