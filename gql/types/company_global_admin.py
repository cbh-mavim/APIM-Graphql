from datetime import date
import strawberry
from typing import Optional
from gql.utils.datetime import DateTimeISO
    
@strawberry.type
class CompanyGlobalAdminType:
    first_name: Optional[str] = strawberry.field(default=None)
    last_name: Optional[str] = strawberry.field(default=None)   
    email: Optional[str] = strawberry.field(default=None)
    user_id: Optional[str] = strawberry.field(default=None)
    role_name: Optional[str] = strawberry.field(default=None)
    role_description: Optional[str] = strawberry.field(default=None)
    user_aggregate_id: Optional[str] = strawberry.field(default=None)
    company_id: Optional[str] = strawberry.field(default=None)
    created: Optional[DateTimeISO] = strawberry.field(default=None)
