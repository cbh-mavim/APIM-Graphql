from typing import Dict,Any
from gql.types import CombinedUsersType
from gql.utils.datetime import parse_mavim_date

def transform_to_combined_users(row: Dict[str, Any]) -> CombinedUsersType:
    return CombinedUsersType(
            user_id=row['user_id'],
            product_name=row['product_name'],
            license_name=row['license_name'],
            user_name=row['user_name'],
            first_name=row['first_name'],
            last_name=row['last_name'],
            created_date=parse_mavim_date(row['created_date']),
            modified_date=parse_mavim_date(row['modified_date']),
            company_id=row['company_id'],
            company_name=row['company_name']            
)
