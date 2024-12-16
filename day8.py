from collections import defaultdict
from itertools import combinations as combs
from copy import deepcopy
from math import gcd

with open(r'inputs\day8.txt') as input_file:
    raw_input = input_file.readlines()
my_roof = [list(line.rstrip('\n')) for line in raw_input]

f_antennae = defaultdict(set)
width = len(my_roof[0])
height = len(my_roof)

for y in range(len(my_roof)):
    for x in range(len(my_roof[0])):
        char = my_roof[y][x]
        if char != ".":
            f_antennae[char].add((y, x))

my_roof_c = deepcopy(my_roof)
my_roof_c2 = deepcopy(my_roof)

for frequency in f_antennae:
    antennae = f_antennae[frequency]
    for pair in combs(antennae, 2):
        a, b = pair
        ax, ay = a
        bx, by = b
        dx = ax - bx
        dy = ay - by
        
        if 0 <= ax + dx < width and 0 <= ay + dy < height:
            my_roof_c[ay+dy][ax+dx] = "#"
        if 0 <= bx - dx < width and 0 <= by - dy < height:
            my_roof_c[by-dy][bx-dx] = "#"
        
        # part 2
        
        d_gcd = gcd(abs(dx), abs(dy))
        dx2, dy2 = dx // d_gcd, dy // d_gcd
        
        while 0 <= ax + dx2 < width and 0 <= ay + dy2 < height:
            my_roof_c2[ay+dy2][ax+dx2] = "#"
            ax += dx2
            ay += dy2
        
        # ??? corner case?
        ax += dx2
        ay += dy2
        
        while 0 <= ax - dx2 < width and 0 <= ay - dy2 < height:
            my_roof_c2[ay-dy2][ax-dx2] = "#"
            ax -= dx2
            ay -= dy2
        
        # bugfix: add the antennae themselves
        my_roof_c2[ay][ax], my_roof_c2[by][bx] = "#", "#"

solution_1 = 0
solution_2 = 0

for y in range(height):
    for x in range(width):
        char = my_roof_c[y][x]
        char_2 = my_roof_c2[y][x]
        if char == "#":
            solution_1 += 1
        if char_2 == "#":
            solution_2 += 1
print(f"Part 1 solution: {solution_1}")
print(f"Part 2 solution: {solution_2}")