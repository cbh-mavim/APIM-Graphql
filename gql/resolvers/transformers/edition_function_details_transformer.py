from typing import Any, Dict
from gql.types import EditionFunctionDetailsType


def transform_to_edition_function_details(
        row: Dict[str, Any]) -> EditionFunctionDetailsType:
    return EditionFunctionDetailsType(
        edition_id=row.get("edition_id"),
        function_id=row.get("function_id"),
        function_code=row.get("function_code"),
        function_name=row.get("function_name"),
        function_description=row.get("function_description"),
        function_subject=row.get("function_subject"),
        function_is_addon=bool(row.get("function_is_addon")),
        function_is_company_wide_addon=bool(
            row.get("function_is_company_wide_addon")),
    )
