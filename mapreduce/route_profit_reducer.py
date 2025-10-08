#!/usr/bin/env python
import sys

route_stats = {}

for line in sys.stdin:
    try:
        route, revenue, distance, rpm = line.strip().split('\t')
        
        if route not in route_stats:
            route_stats[route] = {
                'total_revenue': 0,
                'total_distance': 0,
                'count': 0,
                'rpm_sum': 0
            }
        
        route_stats[route]['total_revenue'] += float(revenue)
        route_stats[route]['total_distance'] += float(distance)
        route_stats[route]['count'] += 1
        route_stats[route]['rpm_sum'] += float(rpm)
    except:
        continue

# Output aggregated results
for route, stats in sorted(route_stats.items(), 
                           key=lambda x: x[1]['total_revenue'], 
                           reverse=True)[:100]:  # Top 100 routes
    avg_rpm = stats['rpm_sum'] / stats['count']
    print(f"{route}\t{stats['total_revenue']:.2f}\t{stats['count']}\t{avg_rpm:.2f}")
