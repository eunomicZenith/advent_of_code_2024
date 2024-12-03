import re

with open(r'inputs\day3.txt') as input_file:
    raw_input = input_file.read()

# find all the multiplications, do's and don'ts
operators = re.finditer(r"mul\((\d+)\,(\d+)\)|do\(\)|don't\(\)", raw_input)

# a bit of setup
total_mult = 0
total_active_mult = 0
enabled = True

# go through every mult/do/don't, one by one
for op in operators:
    
    # switch enabled/disabled when you meet the relevant command
    if op[0] == "do()":
        enabled = True
    elif op[0] == "don't()":
        enabled = False
    
    # when you meet a multiplication...
    else:
        
        # always add its result to total_mult
        a, b = op.groups()
        total_mult += int(a) * int(b)
        
        # only add its result to total_active_mult if enabled
        if enabled:
            total_active_mult += int(a) * int(b)

print(f"Part 1 solution: {total_mult}")
print(f"Part 2 solution: {total_active_mult}")