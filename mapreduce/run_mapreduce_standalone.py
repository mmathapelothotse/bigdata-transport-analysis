#!/usr/bin/env python
"""
Standalone MapReduce Runner
This simulates MapReduce using Python
"""

import os
import sys
import glob
from collections import defaultdict
from datetime import datetime

# Create output directory
os.makedirs('bigdata-transport-analysis\data\output', exist_ok=True)

print("=" * 70)
print("MAPREDUCE PIPELINE")
print("=" * 70)


# ============================================================================
# JOB 1: TIPPING BEHAVIOR ANALYSIS
# ============================================================================
def tipping_mapper(line):
    """Map function: Analyze tipping patterns"""
    try:
        fields = line.strip().split(',')
        if len(fields) < 9:
            return None
            
        trip_distance = float(fields[8])
        fare_amount = float(fields[9])
        tip_amount = float(fields[12])
        payment_type = fields[17]
        
        if fare_amount <= 0:
            return None
            
        tip_percentage = (tip_amount / fare_amount) * 100
        
        # Categorize trip distance
        if trip_distance < 2:
            distance_category = "short"
        elif trip_distance < 10:
            distance_category = "medium"
        else:
            distance_category = "long"
        
        return (payment_type, distance_category, tip_percentage)
    except:
        return None

def tipping_reducer(mapped_data):
    """Reduce function: Calculate average tips"""
    aggregates = defaultdict(lambda: {'sum': 0, 'count': 0})
    
    for item in mapped_data:
        if item:
            payment_type, distance_cat, tip_pct = item
            key = f"{payment_type}\t{distance_cat}"
            aggregates[key]['sum'] += tip_pct
            aggregates[key]['count'] += 1
    
    results = {}
    for key, values in aggregates.items():
        avg_tip = values['sum'] / values['count'] if values['count'] > 0 else 0
        results[key] = f"{avg_tip:.2f}\t{values['count']}"
    
    return results

# ============================================================================
# JOB 2: ROUTE PROFITABILITY ANALYSIS
# ============================================================================
def route_profit_mapper(line):
    """Map function: Calculate route profitability"""
    try:
        fields = line.strip().split(',')
        if len(fields) < 8:
            return None
        
        pickup_loc = fields[5]
        dropoff_loc = fields[6]
        trip_distance = float(fields[8])
        total_amount = float(fields[16])
        
        if trip_distance <= 0:
            return None
            
        revenue_per_mile = total_amount / trip_distance
        route = f"{pickup_loc}-{dropoff_loc}"
        
        return (route, total_amount, trip_distance, revenue_per_mile)
    except:
        return None

def route_profit_reducer(mapped_data):
    """Reduce function: Aggregate route statistics"""
    route_stats = defaultdict(lambda: {
        'total_revenue': 0,
        'total_distance': 0,
        'count': 0,
        'rpm_sum': 0
    })
    
    for item in mapped_data:
        if item:
            route, revenue, distance, rpm = item
            route_stats[route]['total_revenue'] += revenue
            route_stats[route]['total_distance'] += distance
            route_stats[route]['count'] += 1
            route_stats[route]['rpm_sum'] += rpm
    
    # Sort by total revenue and get top 100
    sorted_routes = sorted(route_stats.items(), 
                          key=lambda x: x[1]['total_revenue'], 
                          reverse=True)[:100]
    
    results = {}
    for route, stats in sorted_routes:
        avg_rpm = stats['rpm_sum'] / stats['count'] if stats['count'] > 0 else 0
        results[route] = f"{stats['total_revenue']:.2f}\t{stats['count']}\t{avg_rpm:.2f}"
    
    return results

# ============================================================================
# MAIN EXECUTION ENGINE
# ============================================================================
def run_mapreduce_job(job_name, mapper_func, reducer_func, output_file):
    """Execute a complete MapReduce job"""
    print(f"\n{'=' * 70}")
    print(f"JOB: {job_name}")
    print(f"{'=' * 70}")
    
    # Find input files
    csv_files = glob.glob('bigdata-transport-analysis\data\output\green_tripdata_*.csv')
    
    if not csv_files:
        print("❌ ERROR: No CSV files found in data/output/")
        print("   Please run: python convert_parquet_to_csv.py first")
        return False
    
    print(f"📁 Found {len(csv_files)} input file(s)")
    
    # MAP PHASE
    print("🗺️  MAP Phase: Processing records...")
    mapped_data = []
    total_lines = 0
    
    for csv_file in csv_files:
        with open(csv_file, 'r', encoding='utf-8') as f:
            for line in f:
                total_lines += 1
                result = mapper_func(line)
                if result:
                    mapped_data.append(result)
                
                if total_lines % 1000000 == 0:
                    print(f"   Processed {total_lines:,} lines... ({len(mapped_data):,} valid)")
    
    print(f"✓ MAP Complete: {total_lines:,} lines → {len(mapped_data):,} mapped records")
    
    # SHUFFLE & SORT (implicit in Python data structures)
    print("🔀 SHUFFLE & SORT Phase...")
    
    # REDUCE PHASE
    print("📊 REDUCE Phase: Aggregating results...")
    reduced_data = reducer_func(mapped_data)
    
    print(f"✓ REDUCE Complete: {len(reduced_data)} unique keys")
    
    # OUTPUT
    print(f"💾 Writing results to {output_file}...")
    with open(output_file, 'w', encoding='utf-8') as f:
        for key, value in reduced_data.items():
            f.write(f"{key}\t{value}\n")
    
    print(f"✅ Job completed successfully!")
    return True

# ============================================================================
# MAIN PROGRAM
# ============================================================================
if __name__ == "__main__":
    print("\n🚀 Starting MapReduce Pipeline...")
    print(f"📅 Timestamp: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    
    jobs = [
        ("Tipping Behavior Analysis", tipping_mapper, tipping_reducer, 
         "bigdata-transport-analysis/data/output/tipping_behavior.txt"),
        
        ("Route Profitability Analysis", route_profit_mapper, route_profit_reducer, 
         "bigdata-transport-analysis/data/output/route_profitability.txt")

    ]
    
    success_count = 0
    for job_name, mapper, reducer, output in jobs:
        if run_mapreduce_job(job_name, mapper, reducer, output):
            success_count += 1
    
    print("\n" + "=" * 70)
    print(f"🎉 PIPELINE COMPLETE: {success_count}/{len(jobs)} jobs successful")
    print("=" * 70)
    
    # Show output file sizes
    print("\n📈 Output Summary:")
    for _, _, _, output in jobs:
        if os.path.exists(output):
            size = os.path.getsize(output)
            lines = sum(1 for _ in open(output))
            print(f"   {output}: {size:,} bytes, {lines:,} lines")
