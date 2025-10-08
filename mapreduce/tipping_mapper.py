#!/usr/bin/env python
import sys

for line in sys.stdin:
    try:
        fields = line.strip().split(',')
        trip_distance = float(fields[4])
        fare_amount = float(fields[5])
        tip_amount = float(fields[6])
        payment_type = fields[8]
        
        if fare_amount > 0:
            tip_percentage = (tip_amount / fare_amount) * 100
            
            # Categorize trip distance
            if trip_distance < 2:
                distance_category = "short"
            elif trip_distance < 10:
                distance_category = "medium"
            else:
                distance_category = "long"
            
            # Emit: payment_type-distance_category, tip_percentage
            print(f"{payment_type}\t{distance_category}\t{tip_percentage}")
    except:
        continue
