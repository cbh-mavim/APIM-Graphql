import strawberry
from typing import Optional
from datetime import datetime
    

@strawberry.type
class PortalType:
    portal_id: int
    customer_id: int
    name: str
    connection_string: Optional[str]
    portal_sql_server: Optional[str]
    portal_sql_database: Optional[str]
    portal_sql_user: Optional[str]
    portal_sql_password: Optional[str]
    database_size_mb: Optional[int]
    allowed_db_size_mb: Optional[int]
    portal_app_name: Optional[str]
    portal_app_id: Optional[str]
    portal_url: Optional[str]
    number_of_portal_users: Optional[int]
    portal_users_active: Optional[int]
    created_date: Optional[datetime]
    modified_date: Optional[datetime]
    termination_date: Optional[datetime]
    