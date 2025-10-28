from typing import Any, Dict
from gql.types import CustomerEditionDetailsType


def transform_to_customer_edition_details(
        row: Dict[str, Any]) -> CustomerEditionDetailsType:
    return CustomerEditionDetailsType(
        customer_id=row.get("customer_id"),
        customer_edition_id=row.get("customer_edition_id"),
        edition_id=row.get("customer_edition_edition_id"),
        edition_name=row.get("mavim_edition_name"),
        edition_description=row.get("mavim_edition_description"),
        edition_is_active=bool(row.get("mavim_edition_is_active")),
        edition_quantity=row.get("customer_edition_quantity"),
        edition_created_date=row.get("mavim_edition_created_date"),
        edition_modified_date=row.get("mavim_edition_modified_date"),
        edition_deleted_date=row.get("mavim_edition_deleted_date"),
    )
