from datetime import date
import strawberry
from typing import Optional
from gql.utils.datetime import DateTimeISO
    
@strawberry.type
class CombinedDatabasesType:
    database_id: str
    connection_string: Optional[str]
    database_name: Optional[str]
    company_guid: Optional[str]
    created_date: Optional[DateTimeISO]
    modified_date: Optional[DateTimeISO]
    primary_region: Optional[str]
    company_id: Optional[str]
    company_name: Optional[str]
    reference_db: Optional[str]
    allowed_db_size_mb: Optional[str]
    db_size_mb: Optional[str]
    customer_name_and_id:Optional[str]