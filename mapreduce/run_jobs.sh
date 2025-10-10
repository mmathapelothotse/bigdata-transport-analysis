#!/bin/bash

# Job 1: Tipping Behavior
echo "Running Tipping Analysis..."
cat data/input/green_taxi_*.csv | \
python3 mapreduce/tipping_mapper.py | \
sort | \
python3 mapreduce/tipping_reducer.py > data/output/tipping_behavior.txt

# Job 2: Route Profitability
echo "Running Route Profitability Analysis..."
cat data/input/green_taxi_*.csv | \
python3 mapreduce/route_profit_mapper.py | \
sort | \
python3 mapreduce/route_profit_reducer.py > data/output/route_profitability.txt

echo "All MapReduce jobs completed!"

