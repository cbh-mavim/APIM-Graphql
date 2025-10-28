import strawberry
from typing import Optional
from gql.utils.datetime import DateTimeISO
    
@strawberry.type
class UserMavimManagerLicenseType:
    customer_id: int
    edition_id: Optional[int]
    edition_name: Optional[str]
    user_id: Optional[int]
    user_name: Optional[str]
    first_name: Optional[str]
    last_name: Optional[str]
    deployment_status: Optional[str]
    upn: Optional[str]
    email_address: Optional[str]
    customer_edition_id: Optional[str]
    created_date: Optional[DateTimeISO]
    modified_date: Optional[DateTimeISO]
    deleted_date: Optional[DateTimeISO]
    license_changed_date: Optional[DateTimeISO]
    license: Optional[str]
    
    
    
