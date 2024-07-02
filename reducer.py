#!/usr/bin/env python3

import sys

current_category = None
current_count = 0

# Input comes from stdin (standard input)
for line in sys.stdin:
    # Remove leading/trailing whitespace and split by tab
    line = line.strip()
    
    # Skip empty lines
    if not line:
        continue
    
    # Split the line into category and count
    category_count = line.split('\t')
    
    # Check if the line has both category and count
    if len(category_count) != 2:
        print(f"Ignore invalid input: {line}", file=sys.stderr)
        continue
    
    category, count = category_count
    
    # Convert count to integer
    try:
        count = int(count)
    except ValueError:
        # Ignore if count is not an integer
        print(f"Ignore invalid count: {count}", file=sys.stderr)
        continue
    
    # Process the same category
    if current_category == category:
        current_count += count
    else:
        # Print result for previous category
        if current_category:
            print(f"{current_category}\t{current_count}")
        # Update to new category
        current_category = category
        current_count = count


if current_category:
    print(f"{current_category}\t{current_count}")


