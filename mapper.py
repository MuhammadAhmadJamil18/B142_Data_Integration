#!/usr/bin/env python3

import sys

# Skip the header row
next(sys.stdin)

# Input comes from stdin (standard input)
for line in sys.stdin:
    # Remove leading/trailing whitespace and split by comma
    line = line.strip()
    fields = line.split(',')
    
    # structure based on integrated dataset
    if len(fields) == 12:  
        date = fields[0].strip()
        time = fields[1].strip()
        item_code = fields[2].strip()
        quantity_sold = float(fields[3].strip())
        unit_price = float(fields[4].strip())
        sale_return = fields[5].strip()
        discount = fields[6].strip()
        item_name = fields[7].strip()
        category_code = fields[8].strip()
        category_name = fields[9].strip()
        wholesale_price = float(fields[10].strip())
        loss_rate = float(fields[11].strip())
        
        # Emit key-value pair: (category_name, 1)
        print(f"{category_name}\t1")

