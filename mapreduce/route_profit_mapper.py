#!/usr/bin/env python
import sys

for line in sys.stdin:
    try:
        fields = line.strip().split(',')
        pickup_loc = fields[1]
        dropoff_loc = fields[2]
        total_amount = float(fields[7])
        trip_distance = float(fields[4])
        
        if trip_distance > 0:
            revenue_per_mile = total_amount / trip_distance
            route = f"{pickup_loc}-{dropoff_loc}"
            
            print(f"{route}\t{total_amount}\t{trip_distance}\t{revenue_per_mile}")
    except:
        continue
