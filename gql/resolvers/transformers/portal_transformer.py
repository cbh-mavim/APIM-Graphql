from typing import Any, Dict
from gql.types import PortalType


def transform_to_portal(row: Dict[str, Any]) -> PortalType:
    return PortalType(
        portal_id=row.get("portal_id", ""),
        customer_id=row.get("customer_id", ""),
        name=row.get("portal_name", ""),
        connection_string=row.get("portal_connection_string", ""),
        portal_sql_server=row.get("portal_sql_server", ""),
        portal_sql_database=row.get("portal_sql_database", ""),
        portal_sql_user=row.get("portal_sql_user", ""),
        portal_sql_password=row.get("portal_sql_password", ""),
        database_size_mb=row.get("portal_database_size_mb", 0),
        allowed_db_size_mb=row.get("portal_allowed_db_size_mb", 0),
        portal_app_name=row.get("portal_app_name", ""),
        portal_app_id=row.get("portal_app_id", ""),
        portal_url=row.get("portal_url", ""),
        number_of_portal_users=row.get("portal_number_of_portal_users", 0),
        portal_users_active=row.get("portal_users_active", 0),
        created_date=row.get("portal_created_date", ""),
        modified_date=row.get("portal_modified_date", ""),
        termination_date=row.get("portal_termination_date", ""),
    )
