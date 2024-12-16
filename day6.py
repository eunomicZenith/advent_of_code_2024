import copy
from collections import defaultdict

with open(r'inputs\day6.txt') as input_file:
    raw_input = input_file.readlines()
my_map = [list(line.rstrip('\n')) for line in raw_input]

# bunch of setup
sx, sy = None, None
height = len(my_map)
width = len(my_map[0])
arrows = ['^', '>', 'v', '<']
dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)]


# find the guard's starting coords
for j in range(height):
    for k in range(width):
        if my_map[j][k] == "^":
            sy, sx = j, k


def mazerun(lab, x, y, part=1):
    dir_id = 0
    
    # making a dictionary of how many times we've visited a spot
    if part == 2:
        visits = defaultdict(lambda: 0)
    
    # as long as we're stuck in the maze...
    while True:
        # tentatively shift the coordinates by the shifts of the given direction
        y_shift, x_shift = dirs[dir_id]
        next_x = x + x_shift
        next_y = y + y_shift
        # check if the new spot would still be within the boundaries of the map
        if 0 <= next_x < width and 0 <= next_y < height:
            # check if we're bumping into an obstacle; if so, change direction
            if lab[next_y][next_x] == "#":
                dir_id = (dir_id + 1) % 4
            else:
                # if you don't bump into anything, update the coords
                x, y = next_x, next_y
                
                # keep track of visited spaces and check for loops
                if part == 2:
                    visits[(x, y)] += 1
                    # if we've been somewhere 4 times... that's a loop
                    if visits[(x, y)] > 3:
                        return True
                
                # lay down arrows where we've been
                if part == 1:
                    lab[y][x] = arrows[dir_id]
        else:
            break
    
    # count the arrows to know how many places we've been
    if part == 1:
        visited_spaces = 0
        for line in lab:
            for space in line:
                if space in arrows:
                    visited_spaces += 1
        
        print(f"Visited spaces: {visited_spaces}")
    return False

map_1 = copy.deepcopy(my_map)
mazerun(map_1, sx, sy)

# part 2

possible_loops = 0

for nx in range(width):
    for ny in range(height):
        # only place potential obstacles in places we normally visit, marked with arrows
        if map_1[ny][nx] in arrows:
            map_c = copy.deepcopy(my_map)
            map_c[ny][nx] = "#"
            if mazerun(map_c, sx, sy, 2):
                possible_loops +=1

print(f"Ways to make a loop: {possible_loops}")