
from gql.types import MavimDatabaseType
from gql.utils.datetime import parse_mavim_date
from typing import Dict, Any

def transform_to_mavim_database_details(row: Dict[str, Any]) -> MavimDatabaseType:
    """Transform a data row to a MavimDatabaseType."""
    return MavimDatabaseType(
        database_id=row["database_id"],
        customer_id=row["customer_id"],
        connection_name=row["mavim_database_connection_name"],
        connection_string=row["mavim_database_connection_string"],
        mavim_sql_server=row["mavim_sql_server"],
        mavim_sql_database=row["mavim_sql_database"],
        mavim_schema=row["mavim_schema"],
        mavim_db_license_code=row["mavim_db_license_code"],
        db_size_mb=row["db_size_mb"],
        created_date=parse_mavim_date(row["mavim_database_created_date"]),
        modified_date=parse_mavim_date(row["mavim_database_modified_date"]),
        deleted_date=parse_mavim_date(row["mavim_database_deleted_date"]),
        allowed_db_size_mb=row["mavim_database_allowed_db_size_mb"],
        template_id=row["mavim_database_template_id"],
        onboarded_to_improve=row["mavim_database_onboarded_to_improve"],
        secondary_connection_string=row[
            "mavim_database_secondary_connection_string"],
        domain_name=row["mavim_database_domain_name"],
        database_guid=row["mavim_database_guid"]
        # is_mavim_admin=(row["manager_database_user_is_mavim_admin"]),
        # is_partner=bool(row["manager_database_user_is_partner"]),
        # manager_database_user_id=row["manager_database_user_id"],
        # manager_database_user_database_id=row["manager_database_user_database_id"]
    )
