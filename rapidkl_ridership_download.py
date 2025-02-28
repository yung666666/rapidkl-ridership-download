import requests
import pandas as pd
from io import BytesIO
import os

# File paths for saving daily and monthly data
parquet_daily_path = "daily_ridership.parquet"
parquet_monthly_path = "monthly_ridership.parquet"

# Function to download and load Parquet data
def download_passenger_volume():
    url = "https://storage.data.gov.my/dashboards/prasarana_timeseries.parquet"

    response = requests.get(url)
    
    if response.status_code == 200:
        # Convert the response content into a BytesIO object
        parquet_data = BytesIO(response.content)
        
        # Read the Parquet file into a Pandas DataFrame
        df = pd.read_parquet(parquet_data, engine='pyarrow')
        
        # Some duplicate rows may have two "passengers" values (one of them is 0), sum them
        df = df.groupby(['service', 'frequency', 'origin', 'destination', 'date'], as_index=False)['passengers'].sum()
        
        # Obtain the daily ridership data
        df_daily = df[df['frequency'] == "daily"][['origin', 'destination', 'date', 'passengers']]
        
        # Obtain the monthly ridership data
        df_monthly = df[df['frequency'] == "monthly"][['origin', 'destination', 'date', 'passengers']]
        
        return df_daily, df_monthly
    else:
        print(f"Failed to download data. Status code: {response.status_code}")
        return None, None

# Function to load existing parquet and append new data
def append_to_parquet(df_new, parquet_path):
    if os.path.exists(parquet_path):
        df_existing = pd.read_parquet(parquet_path)
        df_combined = pd.concat([df_existing, df_new], ignore_index=True)
        df_combined.drop_duplicates(subset=['origin', 'destination', 'date'], keep='last', inplace=True)
    else:
        df_combined = df_new
    
    df_combined.to_parquet(parquet_path, index=False)
    print(f"Updated data saved to {parquet_path}")

# Fetch the data
df_daily, df_monthly = download_passenger_volume()

# Append and save to .parquet files
if df_daily is not None and df_monthly is not None:
    append_to_parquet(df_daily, parquet_daily_path)
    append_to_parquet(df_monthly, parquet_monthly_path)
