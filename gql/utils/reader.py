# Azure Data Reader Utilities
# Clean implementation for reading Delta tables and Parquet files from Azure Storage

import pandas as pd
import polars as pl
from io import BytesIO  
import logging
import os
from azure.storage.blob import BlobServiceClient

log = logging.getLogger(__name__)


# def read_delta_table(file_path: str)->pd.DataFrame:
    # """
    # Reads a Delta table from Azure Data Lake Storage using pandas as intermediate.
    
    # Args:
    #     file_path (str): Path to the Delta table
        
    # Returns:
    #     pl.DataFrame: Polars DataFrame containing the Delta table data
    # """
    # try:
    #     con = duckdb.connect()
    #     con.execute("INSTALL httpfs;")
    #     con.execute("LOAD httpfs;")
    #     con.execute("INSTALL azure;")
    #     con.execute("LOAD azure;")
    #     con.execute("INSTALL delta;")
    #     con.execute("LOAD delta;")

    #     # Set up Azure credentials using Managed Identity
    #     storage_account_name = "mavdatalabdevsa"
    #     # client_id = "50b8b4d2-ce78-4a58-954c-6daffc356ce8"
        
    #     log.info(f"Using storage account: {storage_account_name}")
        
    #     # Set environment variable for user-assigned managed identity
    #     # The credential_chain provider will pick this up automatically
    #     os.environ['AZURE_TENANT_ID'] = "a8a7b605-8a76-4f0a-9282-a2c079c0b926"
        
    #     # When running locally, we want to force usage of Azure CLI credentials.
    #     # The credential_chain provider will default to Managed Identity if it thinks it's available.
    #     # By setting AZURE_EXCLUDE_MANAGED_IDENTITY_CREDENTIAL to "true", we can prevent this.
    #     # In a deployed environment (e.g., Azure Function), this variable should not be set.
    #     if os.getenv("AZURE_FUNCTIONS_ENVIRONMENT") is None:
    #         os.environ["AZURE_EXCLUDE_MANAGED_IDENTITY_CREDENTIAL"] = "true"
    #         log.info("Running locally, excluding Managed Identity from credential chain.")

    #     con.execute(f"""
    #     CREATE OR REPLACE SECRET azure_credentials (
    #         TYPE AZURE,
    #         PROVIDER credential_chain,
    #         ACCOUNT_NAME '{storage_account_name}'
    #     );
    #     """)


    #     if not file_path.startswith("abfss://"):
    #         if file_path.startswith("external/"):
    #             file_path = file_path[9:]  # Remove "external/" prefix
    #         delta_path = f"abfss://external@{storage_account_name}.dfs.core.windows.net/{file_path}/"
    #     else:
    #         delta_path = file_path
        
    #     print(f"Reading Delta table from: {delta_path}")
        
    #     # Read Delta table using delta_scan
    #     df = con.execute(f"SELECT * FROM delta_scan('{delta_path}')").df()
    # except Exception as e:
    #     print(f"Error reading Delta table: {str(e)}")
    #     df = pd.DataFrame({"error": [str(e)]})  # Return DataFrame with error message
    #     raise
    # return df

def read_csv_files_to_polars_df(file_path: str) -> pl.DataFrame:
    # Azure storage account credentials
    connection_string = (
        "DefaultEndpointsProtocol=https;"
        "AccountName=mavdatalabdevsa;"
        "AccountKey=GJjIbQW7QiwpWSUwyFuFN+v7p/o7ZMSM7Yt/UKXcd6IELOMkFipstnptesHlJTSc0dR9nN2fqngT+AStVk0I/A==;"
        "EndpointSuffix=core.windows.net"
    )
    container_name = "external"
   
    # Initialize BlobServiceClient
    blob_service_client = BlobServiceClient.from_connection_string(connection_string)
    container_client = blob_service_client.get_container_client(container_name)

    # Ensure the file_path ends with a slash
    if not file_path.endswith("/"):
        file_path += "/"
    blobs = container_client.list_blobs(name_starts_with=file_path)
    # Read all CSV files into a single Polars DataFrame
    df_list = []
    for blob in blobs:
        if blob.name.endswith(".csv"):
            print(f"Reading CSV file: {blob.name}")
            blob_client = container_client.get_blob_client(blob.name)
            blob_data = blob_client.download_blob().readall()
            df = pl.read_csv(BytesIO(blob_data))
            df_list.append(df)

    # Concatenate all Polars DataFrames
    if df_list:
        final_df = pl.concat(df_list, how="vertical_relaxed")
        return final_df
    else:
        return pl.DataFrame()