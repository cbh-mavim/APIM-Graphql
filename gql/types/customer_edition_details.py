from datetime import datetime
import strawberry
from typing import Optional
      
@strawberry.type
class CustomerEditionDetailsType:
    customer_id: int
    customer_edition_id: int
    edition_id: int
    edition_name: Optional[str]
    edition_description: Optional[str]
    edition_is_active: Optional[bool]
    edition_quantity: Optional[int]
    edition_created_date: Optional[datetime]
    edition_modified_date: Optional[datetime]
    edition_deleted_date: Optional[datetime]
    