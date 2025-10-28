import strawberry
from typing import Optional
from gql.utils.datetime import DateTimeISO
from datetime import date
    
@strawberry.type
class MavimDatabaseType:
    database_id: int
    customer_id: int
    connection_name: str
    connection_string: Optional[str]
    mavim_sql_server: Optional[str]
    mavim_sql_database: Optional[str]
    mavim_schema: Optional[str]
    mavim_db_license_code: Optional[str]
    db_size_mb: Optional[int]
    created_date: Optional[DateTimeISO]
    modified_date: Optional[DateTimeISO]
    deleted_date: Optional[DateTimeISO]
    allowed_db_size_mb: Optional[int]
    template_id: Optional[int]
    onboarded_to_improve: Optional[int]  
    secondary_connection_string: Optional[str]
    domain_name: Optional[str]
    database_guid: Optional[str]
    # is_mavim_admin: Optional[str]
    # is_partner: Optional[bool]
    # manager_database_user_id: Optional[int]
    # manager_database_user_database_id: Optional[int]