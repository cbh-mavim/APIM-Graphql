from datetime import date
import strawberry
from typing import Optional
from gql.utils.datetime import DateTimeISO
    
@strawberry.type
class LicenseCustomerProductType:
    customer_id: int
    customer_name: Optional[str]
    number_of_databases: Optional[int]
    is_partner: Optional[str]
    product_name: Optional[str]
    license_name: Optional[str]
    license_quantity: Optional[int]
    used_qty: Optional[int]
    is_active: Optional[str]
    created:Optional[DateTimeISO]