from typing import Any, Dict
from gql.types import LicenseCustomerProductType
from gql.utils.datetime import parse_mavim_date

def transform_to_license_customer_product(
        row: Dict[str, Any]) -> LicenseCustomerProductType:
    """Transform a data row to a LicenseCustomerProductType."""
    return LicenseCustomerProductType(
        customer_id=row["customer_id"],
        customer_name=row["customer_name"],
        number_of_databases=int(row["number_of_databases"])
        if row["number_of_databases"] is not None else None,
        is_partner=row["is_partner"],
        product_name=row["product_name"],
        license_name=row["license_name"],
        license_quantity=int(row["license_quantity"])
        if row["license_quantity"] is not None else None,
        used_qty=int(row["used_qty"]) if row["used_qty"] is not None else None,
        is_active=row["is_active"],
        created=parse_mavim_date(row['created']))
