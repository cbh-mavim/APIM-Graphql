import typing
import strawberry
from gql.resolvers.query.company_global_admin import get_company_global_admin
from gql.types import (
    UserMavimManagerLicenseType, LicenseCustomerProductType, CompanyType,
    CustomerAddonDetailsType, CustomerEditionDetailsType,
    EditionFunctionDetailsType, MavimDatabaseType, PortalType,MpmCustomerType
    ,CombinedDatabasesType,CombinedUsersType,PortalMonthlyUserReportType
    )
from gql.types.company_global_admin import CompanyGlobalAdminType
from gql.types.manager_user_login_details import ManagerUserLoginDetailsType
from ..resolvers import (get_companies, get_customer_addons_details,
                         get_customer_edition_details,
                         get_edition_function_details,
                         get_mavim_databases_details,
                         get_license_customer_product,
                         get_users_mavim_manager, get_portal,
                         get_mpm_customers,
                        get_combined_databases,
                        get_combined_users,
                        get_portal_monthly_users_report,
                        get_manager_user_login_details
                         )


@strawberry.type
class Query:
    companies: typing.List[CompanyType] = strawberry.field(resolver=get_companies)
    customer_addons_details: typing.List[CustomerAddonDetailsType] = strawberry.field(resolver=get_customer_addons_details)
    customer_edition_details: typing.List[CustomerEditionDetailsType] = strawberry.field(resolver=get_customer_edition_details)
    edition_function_details: typing.List[EditionFunctionDetailsType] = strawberry.field(resolver=get_edition_function_details)
    mavim_databases_details: typing.List[MavimDatabaseType] = strawberry.field(resolver=get_mavim_databases_details)
    users: typing.List[UserMavimManagerLicenseType] = strawberry.field(resolver=get_users_mavim_manager)
    license_customer_product: typing.List[LicenseCustomerProductType] = strawberry.field(resolver=get_license_customer_product)
    portal: typing.List[PortalType] = strawberry.field(resolver=get_portal)
    mpm_customers: typing.List[MpmCustomerType] = strawberry.field(resolver=get_mpm_customers)
    combined_databases: typing.List[CombinedDatabasesType] = strawberry.field(resolver=get_combined_databases)
    combined_users: typing.List[CombinedUsersType] = strawberry.field(resolver=get_combined_users)
    portal_monthly_users_report: typing.List[PortalMonthlyUserReportType] = strawberry.field(resolver=get_portal_monthly_users_report)
    global_admin: typing.List[CompanyGlobalAdminType] = strawberry.field(resolver=get_company_global_admin)
    manager_user_login_details: typing.List[ManagerUserLoginDetailsType] = strawberry.field(resolver=get_manager_user_login_details)
