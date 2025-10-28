from typing import Any, Dict
from gql.types import CompanyGlobalAdminType
from gql.utils.datetime import parse_mavim_date


def transform_to_company_global_admin(
        row: Dict[str, Any]) -> CompanyGlobalAdminType:

    return CompanyGlobalAdminType(
        first_name=row.get('FirstName'),
        last_name=row.get('LastName'),
        email=row.get('Email'),
        user_id=row.get('user_id'),
        role_name=row.get('role_name'),
        role_description=row.get('role_description'),
        user_aggregate_id=row.get('user_aggregateid'),
        company_id=row.get('CompanyId'),
        created=row.get('Created')
        )
    

