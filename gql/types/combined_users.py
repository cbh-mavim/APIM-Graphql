from datetime import date
import strawberry
from typing import Optional
from gql.utils.datetime import DateTimeISO
    
@strawberry.type
class CombinedUsersType:
    user_id: str
    product_name: Optional[str]
    license_name: Optional[str]
    user_name: Optional[str]
    first_name: Optional[str]
    last_name: Optional[str]
    created_date: Optional[DateTimeISO]
    modified_date: Optional[DateTimeISO]
    company_id: Optional[str]
    company_name: Optional[str]

    
