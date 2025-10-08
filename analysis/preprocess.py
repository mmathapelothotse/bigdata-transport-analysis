import os
import glob
import pandas as pd

def convert_parquet_to_csv():
    """Convert multiple Parquet files to a single CSV for Hadoop MapReduce."""
    input_dir = 'data/input'
    parquet_files = glob.glob(os.path.join(input_dir, '*.parquet'))

    combined_csv = os.path.join(input_dir, 'yellow_taxi_combined.csv')
    # Remove existing combined file if it exists
    if os.path.exists(combined_csv):
        os.remove(combined_csv)

    first = True
    for file in parquet_files:
        print(f'Reading {file}...')
        df = pd.read_parquet(file)
        df_subset = df[['tpep_pickup_datetime', 'PULocationID', 'DOLocationID', 
                        'passenger_count', 'trip_distance', 'fare_amount', 
                        'tip_amount', 'total_amount', 'payment_type']]
        if first:
            df_subset.to_csv(combined_csv, index=False, mode='w', header=True)
            first = False
        else:
            df_subset.to_csv(combined_csv, index=False, mode='a', header=False)
        print(f'Appended {file} to {combined_csv}')

    if not parquet_files:
        print('No parquet files found.')
    else:
        print(f'All {len(parquet_files)} files have been combined into {combined_csv}')

if __name__ == "__main__":
    convert_parquet_to_csv()
