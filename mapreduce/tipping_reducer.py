#!/usr/bin/env python
import sys

current_key = None
tip_sum = 0
count = 0

for line in sys.stdin:
    try:
        payment_type, distance_cat, tip_pct = line.strip().split('\t')
        key = f"{payment_type}\t{distance_cat}"
        
        if current_key == key:
            tip_sum += float(tip_pct)
            count += 1
        else:
            if current_key and count > 0:
                avg_tip = tip_sum / count
                print(f"{current_key}\t{avg_tip:.2f}\t{count}")
            current_key = key
            tip_sum = float(tip_pct)
            count = 1
    except:
        continue

if current_key and count > 0:
    avg_tip = tip_sum / count
    print(f"{current_key}\t{avg_tip:.2f}\t{count}")
