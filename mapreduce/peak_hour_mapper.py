#!/usr/bin/env python
import sys
from datetime import datetime

for line in sys.stdin:
    try:
        fields = line.strip().split(',')
        pickup_time = fields[0]
        location_id = fields[1]
        
        # Extract hour from timestamp
        dt = datetime.fromisoformat(pickup_time.replace(' ', 'T'))
        hour = dt.hour
        
        # Emit: hour-location as key, count as value
        print(f"{hour}\t{location_id}\t1")
        
    except Exception as e:
        continue
