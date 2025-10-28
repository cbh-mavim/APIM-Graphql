from datetime import date
import strawberry
from typing import Optional
from gql.utils.datetime import DateTimeISO
    
@strawberry.type
class MpmCustomerType:
    customer_id: int
    number_of_analyzer: Optional[int]
    number_of_developer: Optional[int]
    number_of_reports: Optional[int]
    workspace_id: Optional[str]
    portal_url: Optional[str]
    subscription_key: Optional[str]
    subscription_start_date: Optional[str]
    subscription_end_date: Optional[str]