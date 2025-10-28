from typing import Any, Dict
from gql.types import UserMavimManagerLicenseType


def transform_to_user_mavim_manager_license(
        row: Dict[str, Any]) -> UserMavimManagerLicenseType:
    return UserMavimManagerLicenseType(
        customer_edition_id=row["customer_edition_id"],
        customer_id=row["customer_id"],
        deployment_status=row["deployment_status"],
        edition_id=row["edition_id"],
        edition_name=row["edition_name"],
        email_address=row["email_address"],
        first_name=row["first_name"],
        last_name=row["last_name"],
        upn=row["upn"],
        user_name=row["user_name"],
        created_date=row["created_date"],
        user_id=row["user_id"],
        modified_date=row["modified_date"],
        deleted_date=row["deleted_date"],
        license_changed_date=row["license_changed_date"],
        license=row["license"])

# print(transform_to_mavim_manager_license({
#     "customer_edition_id": "12345",
#     "customer_id": "67890",
#     "deployment_status": "active",
#     "edition_id": "ed123",
#     "edition_name": "Standard Edition",
#     "email_address": "",
#     "first_name": "John",
    
#     "last_name": "Doe",
#     "upn": "sa",
#     "user_name": "johndoe",
#     "created_date": "2023-01-01",
#     "user_id": "user123",
#     "modified_date": "2023-01-02",
#     "deleted_date": None,
#     "license_changed_date": "2023-01-03",
#     "license": "premium"}    
    
# ))