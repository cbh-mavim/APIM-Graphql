from typing import Any, Dict
from gql.types import ManagerUserLoginDetailsType


def transform_to_manager_user_login_details(
        row: Dict[str, Any]) -> ManagerUserLoginDetailsType:
    return ManagerUserLoginDetailsType(
        id=row["id"],
        thinfinity_user=row["thinfinity_user"],
        customer_id=row["customer_id"],
        login_time=row["login_time"]
    )
