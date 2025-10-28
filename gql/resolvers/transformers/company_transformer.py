from typing import Dict, Any
from gql.types import CompanyType

def transform_to_company(row: Dict[str, Any]) -> CompanyType:
    """Transform a data row to a CompanyType."""
    return CompanyType(
        customer_id=row["customer_id"],
        customer_name=row["customer_name"],
        created_date=row["created_date"],
        modified_date=row["modified_date"],
        termination_date=row["termination_date"],
        terminated_date=row["terminated_date"],
        crm_id=row["crm_id"],
        number_of_databases=row["number_of_databases"],
        number_of_portal_users=row["number_of_portal_users"],
        external_customer_id=row["external_customer_id"],
        is_partner=bool(row["is_partner"]),
        partner_customer_id=row["partner_customer_id"],
        is_onboarded_to_improve=bool(row["is_onboarded_to_improve"]),
        onboarded_to_improve_date=row["onboarded_to_improve_date"],
        exact_id=row["exact_id"],
        version_number=row["version_number"],
        company_guid=row["company_guid"],
        domain_name=row["domain_name"],
        app_id=row["app_id"],
        customer_name_and_id=row["customer_name_and_id"],
        crm_url=row["crm_url"]
    )

