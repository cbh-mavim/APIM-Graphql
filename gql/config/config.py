import os
from pathlib import Path
import yaml
from typing import Dict, Any

# Get the directory containing the current script
CONFIG_DIR: Path = Path(__file__).parent

# Load the YAML file using absolute path
with open(CONFIG_DIR/'config.yaml', 'r', encoding='utf-8') as file:
    config: Dict[str, Any] = yaml.safe_load(file)
 
 
 ## get the keys of the tables from the config file
tables_names = config.get('tables', {}).keys()
    
# Access the base directory
base_dir =(config['base_dir'])
# Define data directories - convert Path objects to strings for PySpark compatibility
combined_databases: str = str(base_dir+ "/"+ 'combined_databases')
combined_users: str = str(base_dir+ "/"+ 'combined_users')
company: str = str(base_dir+ "/"+ 'company')
customer_addon_details: str = str(base_dir+ "/"+ 'customer_addon_details')
customer_edition_details: str = str(base_dir+ "/"+ 'customer_edition_details')
edition_function_details: str = str(base_dir+ "/"+ 'edition_function_details')
license_customer_product: str = str(base_dir+ "/"+ 'license_customer_product')
mavim_databases_details: str = str(base_dir+ "/"+ 'mavim_databases_details')
mpm_customers: str = str(base_dir+ "/"+ 'mpm_customers')
portal_monthly_users_report: str = str(base_dir+ "/"+ 'portal_monthly_users_report')
company_global_admins: str = str(base_dir+ "/"+ 'company_global_admins')
portal: str = str(base_dir+ "/"+ 'portal')
users: str = str(base_dir+ "/"+ 'mavim_manager_users')
manager_user_login_details: str = str(base_dir+ "/"+ 'manager_user_login_details')