#!/usr/bin/env python3

from gql.utils.reader import read_delta_table
import polars as pl

# Test reading delta table
print("Testing Delta table reading...")
df = read_delta_table('mavim_catalog/gold/portal_monthly_users_report')
print(f'Data type: {type(df)}')
print(f'Shape: {df.shape if hasattr(df, "shape") else "N/A"}')

# Test conversion to Polars if needed
if hasattr(df, 'iterrows'):  # Pandas DataFrame
    print("Converting Pandas to Polars...")
    df_polars = pl.from_pandas(df)
    print(f'Polars DataFrame shape: {df_polars.shape}')
    print(f'First row: {dict(next(df_polars.iter_rows(named=True)))}')
else:
    print("Already a Polars DataFrame")