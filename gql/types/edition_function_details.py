import strawberry
from typing import Optional

@strawberry.type
class EditionFunctionDetailsType:
    edition_id: int
    function_id: int
    function_code: Optional[str]
    function_name: Optional[str]
    function_description: Optional[str]
    function_subject: Optional[str]
    function_is_addon: Optional[bool]
    function_is_company_wide_addon: Optional[bool]