from typing import Any, Dict
from gql.types import MpmCustomerType

def transform_to_mpm_customer(row: Dict[str, Any]) -> MpmCustomerType:
    """Transform a data row to a MpmCustomerType."""
    return MpmCustomerType(
        customer_id=row["customer_id"],
        number_of_analyzer=row["number_of_analyzer"],
        number_of_developer=row["number_of_developer"],
        number_of_reports=row["number_of_reports"],
        workspace_id=row["workspace_id"],
        portal_url=row["portal_url"],
        subscription_key=row["subscription_key"],
        subscription_start_date=row["subscription_start_date"],
        subscription_end_date=row["subscription_end_date"],
    )
