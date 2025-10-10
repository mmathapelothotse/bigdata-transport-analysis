import os
import pandas as pd
import subprocess

input_dir = 'bigdata-transport-analysis\data\input'
output_dir = 'bigdata-transport-analysis\data\output'
hdfs_output_dir = '/nyc_tlc_data/data/output/'

# Hadoop streaming JAR path (update if different)
HADOOP_STREAMING_JAR = "/usr/local/hadoop/share/hadoop/tools/lib/hadoop-streaming-3.4.2.jar"



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
            df.head(1000).to_csv(out_path, index=False)
            print(f"Successfully wrote {len(df)} rows.")
       
            # Upload CSV to HDFS
            print(f"Uploading {out_path} to HDFS directory {hdfs_output_dir}...")
            subprocess.run(["hdfs", "dfs", "-mkdir", "-p", hdfs_output_dir])
            subprocess.run(["hdfs", "dfs", "-put", "-f", out_path, hdfs_output_dir])
            print(f"Uploaded {out_fname} to HDFS successfully.")

        except Exception as e:
            print(f"Failed to convert {fname}: {e}")


