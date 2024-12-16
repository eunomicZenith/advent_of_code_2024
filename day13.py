import numpy as np
import re

with open(r'inputs\day13.txt') as input_file:
    raw_input = input_file.readlines()
input_strings = [line.rstrip('\n') for line in raw_input]

machines = []
part_1 = 0
part_2 = 0

# this parses the input; each claw machine just becomes a list of 6 numbers
for i, line in enumerate(input_strings):
    if i % 4 != 3:
        if i % 4 == 0:
            machine = []
        nums = [int(x) for x in re.findall(r"\d+", line)]
        machine.extend(nums)
    if i % 4 == 2:
        machines.append(machine)

for machine in machines:
    # systems of equations fuck yeah
    x1, y1, x2, y2, xt, yt = machine
    a = np.array([[x1, x2],[y1, y2]])
    b = np.array([xt, yt])
    sols = np.linalg.solve(a,b)
    
    # untangling whether these are actually integers from numpy floats is a bit complicated, so I will cheat
    # just round to the nearest integer, then check if the system of equations still checks out
    sa, sb = [int(s) for s in np.rint(sols)]
    if (x1 * sa) + (x2 * sb) == xt and (y1 * sa) + (y2 * sb) == yt:
        part_1 += (sa * 3) + sb
    
    # let's just do this all over again for part 2
    # but this time the goals are increased by 10 trillion!
    xt, yt = xt+10000000000000, yt+10000000000000
    
    a = np.array([[x1, x2],[y1, y2]])
    b = np.array([xt, yt])
    sols = np.linalg.solve(a,b)
    
    sa, sb = [int(s) for s in np.rint(sols)]
    if (x1 * sa) + (x2 * sb) == xt and (y1 * sa) + (y2 * sb) == yt:
        part_2 += (sa * 3) + sb

print(f"Part 1 solution: {part_1}")
print(f"Part 2 solution: {part_2}")