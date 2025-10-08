#!/usr/bin/env python
import sys

current_key = None
current_count = 0

for line in sys.stdin:
    try:
        hour, location, count = line.strip().split('\t')
        key = f"{hour}\t{location}"
        
        if current_key == key:
            current_count += int(count)
        else:
            if current_key:
                print(f"{current_key}\t{current_count}")
            current_key = key
            current_count = int(count)
    except:
        continue

# Output last key
if current_key:
    print(f"{current_key}\t{current_count}")
