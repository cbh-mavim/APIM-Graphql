import strawberry
from typing import Optional
from gql.utils.datetime import DateTimeISO
    
@strawberry.type
class ManagerUserLoginDetailsType:
    id: int
    thinfinity_user: Optional[str]
    customer_id: Optional[int]
    login_time: Optional[DateTimeISO]
