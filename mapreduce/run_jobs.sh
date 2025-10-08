#!/bin/bash

# Job 1: Peak Hour Analysis
echo "Running Peak Hour Analysis..."
cat data/input/yellow_taxi_*.csv | \
python3 mapreduce/peak_hour_mapper.py | \
sort | \
python3 mapreduce/peak_hour_reducer.py > data/output/peak_hours.txt

# Job 2: Tipping Behavior
echo "Running Tipping Analysis..."
cat data/input/yellow_taxi_*.csv | \
python3 mapreduce/tipping_mapper.py | \
sort | \
python3 mapreduce/tipping_reducer.py > data/output/tipping_behavior.txt

# Job 3: Route Profitability
echo "Running Route Profitability Analysis..."
cat data/input/yellow_taxi_*.csv | \
python3 mapreduce/route_profit_mapper.py | \
sort | \
python3 mapreduce/route_profit_reducer.py > data/output/route_profitability.txt

echo "All MapReduce jobs completed!"
