from .company import CompanyType
from .customer_addons_details import CustomerAddonDetailsType
from .customer_edition_details import CustomerEditionDetailsType
from .edition_function_details import EditionFunctionDetailsType
from .mavim_databases_details import MavimDatabaseType
from .users import UserMavimManagerLicenseType
from .mpm_customers import MpmCustomerType
from .portal import PortalType
from .license_customer_product import LicenseCustomerProductType
from .combined_databases import CombinedDatabasesType
from .combined_users import CombinedUsersType
from .portal_monthly_users_report import PortalMonthlyUserReportType
from .company_global_admin import CompanyGlobalAdminType
from .manager_user_login_details import ManagerUserLoginDetailsType
    
# @strawberry.type
# class CompanyType:
#     customer_id: int
#     customer_name: Optional[str]
#     created_date: Optional[DateTimeISO]
#     modified_date: Optional[DateTimeISO]
#     termination_date: Optional[DateTimeISO]
#     terminated_date: Optional[DateTimeISO]
#     crm_id: Optional[str]
#     number_of_databases: Optional[int]
#     number_of_portal_users: Optional[int]
#     external_customer_id: Optional[str]
#     is_partner: Optional[bool]
#     partner_customer_id: Optional[int]
#     is_onboarded_to_improve: Optional[bool]
#     onboarded_to_improve_date: Optional[DateTimeISO]
#     exact_id: Optional[float]
#     version_number: Optional[str]
#     company_guid: Optional[str]
#     domain_name: Optional[str]
#     app_id: Optional[str]
    

    
# @strawberry.type
# class CustomerEditionDetailsType:
#     customer_id: int
#     customer_edition_id: int
#     edition_id: int
#     edition_name: Optional[str]
#     edition_description: Optional[str]
#     edition_is_active: Optional[bool]
#     edition_quantity: Optional[int]
#     edition_created_date: Optional[DateTimeISO]
#     edition_modified_date: Optional[DateTimeISO]
#     edition_deleted_date: Optional[DateTimeISO]
    

# @strawberry.type
# class EditionFunctionDetailsType:
#     edition_id: int
#     function_id: int
#     function_code: Optional[str]
#     function_name: Optional[str]
#     function_description: Optional[str]
#     function_subject: Optional[str]
#     function_is_addon: Optional[bool]
#     function_is_company_wide_addon: Optional[bool]

# @strawberry.type
# class CustomerAddonDetailsType:
#     customer_id: Optional[int]
#     addon_id: Optional[int]
#     quantity: Optional[int]
#     addon_configuration: Optional[str]
#     customer_addon_id: Optional[int]
#     name: Optional[str]
#     is_addon: Optional[bool]

    
# @strawberry.type
# class MavimDatabaseType:
#     database_id: int
#     customer_id: int
#     connection_name: str
#     connection_string: Optional[str]
#     mavim_sql_server: Optional[str]
#     mavim_sql_database: Optional[str]
#     mavim_schema: Optional[str]
#     mavim_db_license_code: Optional[str]
#     db_size_mb: Optional[int]
#     created_date: Optional[DateTimeISO]
#     modified_date: Optional[DateTimeISO]
#     deleted_date: Optional[DateTimeISO]
#     allowed_db_size_mb: Optional[int]
#     template_id: Optional[int]
#     onboarded_to_improve: Optional[int]  
#     secondary_connection_string: Optional[str]
#     domain_name: Optional[str]
#     database_guid: Optional[str]
#     is_mavim_admin: Optional[bool]
#     is_partner: Optional[bool]
#     mavim_user_username: Optional[str] 
#     mavim_user_first_name: Optional[str]
#     mavim_user_last_name: Optional[str]
#     mavim_user_mavim_function_old: Optional[str]
#     mavim_user_created_date: Optional[DateTimeISO]
#     mavim_user_modified_date: Optional[DateTimeISO]
#     mavim_user_deleted_date: Optional[DateTimeISO]
#     mavim_user_license_changed_date: Optional[DateTimeISO]
#     mavim_user_customer_edition_id: Optional[str]
#     mavim_user_license: Optional[str]
#     mavim_user_deployment_status: Optional[str]
#     mavim_user_upn: Optional[str]
#     mavim_user_email_address: Optional[str]
    
# @strawberry.type
# class MavimUserType:
#     user_id: int
#     customer_id: int
#     user_name: str
#     license: Optional[str]
#     first_name: Optional[str]
#     last_name: Optional[str]
#     deployment_status: Optional[str]
#     upn: Optional[str]
#     mavim_function_old: Optional[str]
#     email_address: Optional[str]
#     created_date: Optional[DateTimeISO]
#     modified_date: Optional[DateTimeISO]
#     deleted_date: Optional[DateTimeISO]
#     license_changed_date: Optional[DateTimeISO]
#     customer_edition_id: Optional[str]
    
# @strawberry.type
# class PortalType:
#     portal_id: int
#     customer_id: int
#     name: str
#     connection_string: Optional[str]
#     portal_sql_server: Optional[str]
#     portal_sql_database: Optional[str]
#     portal_sql_user: Optional[str]
#     portal_sql_password: Optional[str]
#     database_size_mb: Optional[int]
#     allowed_db_size_mb: Optional[int]
#     portal_app_name: Optional[str]
#     portal_app_id: Optional[str]
#     portal_url: Optional[str]
#     number_of_portal_users: Optional[int]
#     portal_users_active: Optional[int]
#     created_date: Optional[DateTimeISO]
#     modified_date: Optional[DateTimeISO]
#     termination_date: Optional[DateTimeISO]
    
# @strawberry.type
# class EditionFunctionType:
#     edition_id: int
#     function_id: int
    
# @strawberry.type
# class ManagerDatabaseUserType:
#     database_user_id: int
#     user_id: int
#     database_id: int
#     is_mavim_admin: Optional[bool]
    
# @strawberry.type
# class MavimEditionType:
#     edition_id: int
#     name: str
#     description: Optional[str]
#     is_active: Optional[bool]
    
# @strawberry.type
# class MavimFunctionType:
#     function_id: int
#     function_code: str
#     name: str
#     description: str
#     subject: str
#     is_addon: Optional[bool]
#     is_company_wide_addon: Optional[bool]
    
# @strawberry.type
# class PortalMonthlyUsersReportType:
#     report_id: int
#     portal_id: int
#     portal_name: str
#     portal_sql_database: str
#     users_count: Optional[int]
#     month: str
#     year: str
#     report_created_at: Optional[DateTimeISO]
    
# @strawberry.type
# class UserAddonType:
#     user_addon_id: int
#     user_id: int
#     addon_id: int
    
# @strawberry.type
# class MpmCustomerType:
#     customer_id: int
#     number_of_analyzer: Optional[int]
#     number_of_developer: Optional[int]
#     number_of_reports: Optional[int]
#     workspace_id: Optional[str]
#     portal_url: Optional[str]
#     subscription_key: Optional[str]
#     subscription_start_date: Optional[DateTimeISO]
#     subscription_end_date: Optional[DateTimeISO]