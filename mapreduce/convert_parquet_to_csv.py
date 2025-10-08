import os
import pandas as pd

input_dir = 'data\input'
output_dir = 'data\output'

if not os.path.exists(input_dir):
    print(f"Input directory {input_dir} does not exist. Please check the path.")
else:
    os.makedirs(output_dir, exist_ok=True)
    parquet_files = [f for f in os.listdir(input_dir) if f.lower().endswith('.parquet')]
    print(f"Found {len(parquet_files)} Parquet file(s): {parquet_files}")
    for fname in parquet_files:
        in_path = os.path.join(input_dir, fname)
        out_fname = fname.rsplit('.', 1)[0] + '.csv'
        out_path = os.path.join(output_dir, out_fname)
        print(f"Converting {in_path} to {out_path}...")
        try:
            df = pd.read_parquet(in_path)
            df.to_csv(out_path, index=False)
            print(f"Successfully wrote {len(df)} rows.")
        except Exception as e:
            print(f"Failed to convert {fname}: {e}")

