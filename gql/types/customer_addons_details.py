import strawberry
from typing import Optional    

@strawberry.type
class CustomerAddonDetailsType:
    customer_id: Optional[int]
    addon_id: Optional[int]
    quantity: Optional[int]
    addon_configuration: Optional[str]
    customer_addon_id: Optional[int]
    name: Optional[str]
    is_addon: Optional[bool]
