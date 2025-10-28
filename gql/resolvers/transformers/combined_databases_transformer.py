from typing import Any, Dict
from gql.types import CombinedDatabasesType
from gql.utils.datetime import parse_mavim_date


def transform_to_combined_databases(row: Dict[str, Any]) -> CombinedDatabasesType:

    return CombinedDatabasesType(database_id=row['database_id'],
                          connection_string=row['connection_string'],
                          database_name=row['database_name'],
                          company_guid=row['company_guid'],
                          created_date=parse_mavim_date(row['created_date']),
                          modified_date=parse_mavim_date(row['modified_date']),
                          primary_region=row['primary_region'],
                          company_id=row['company_id'],
                          company_name=row['company_name'],
                          reference_db=row['reference_db'],
                          allowed_db_size_mb=row['allowed_db_size_mb'],
                          db_size_mb=row['db_size_mb'],
                          customer_name_and_id=row['customer_name_and_id'])
