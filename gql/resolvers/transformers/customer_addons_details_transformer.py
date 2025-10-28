from typing import Dict, Any
from gql.types import CustomerAddonDetailsType

def transform_to_customer_addons_details(row: Dict[str, Any]) -> CustomerAddonDetailsType:
    """Transform a data row to a CustomerAddonDetailsType."""
    return  CustomerAddonDetailsType(
            customer_id=row["customer_id"],
            addon_id=row["addon_id"],
            quantity=row["quantity"],
            addon_configuration=row["addon_configuration"],
            customer_addon_id=row["customer_addon_id"],
            name=row["name"],
            is_addon=bool(row["is_addon"])
    )