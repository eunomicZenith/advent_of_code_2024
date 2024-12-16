with open(r'inputs\day10.txt') as input_file:
    raw_input = input_file.readlines()
my_map = [[int(n) for n in line.rstrip('\n')] for line in raw_input]

dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)]
height = len(my_map)
width = len(my_map[0])
starts = set()

# let's find all the 0's; they are our starting points
for y, line in enumerate(my_map):
    for x, n in enumerate(line):
        if n == 0:
            starts.add((y, x))


# unified function for both parts
def trailblaze(starting_set, part=1):
    spots_to_search = starting_set.copy()
    
    # making the parallel map for part 2
    if part == 2:
        p_map = [[1 if b == 0 else 0 for b in line] for line in my_map]
    
    # we're using a global tracker for elevation because it increases by 1 with each go anyway, so why not
    elev = 0
    while elev < 9:
        new_spots_to_search = set()
        
        # for each starting spot, check its neighbors...
        for spot in spots_to_search:
            y, x = spot
            for dir in dirs:
                dy, dx = dir
                next_y, next_x = y + dy, x + dx
                
                # avoid stepping outside the map
                if 0 <= next_x < width and 0 <= next_y < height:
                    neighbor = my_map[next_y][next_x]
                    
                    # check if the neighbor is one step higher; if so, it's valid, so add it to the new spots to search next!
                    if neighbor == elev + 1:
                        new_spots_to_search.add((next_y, next_x))
                        
                        # if it's p2, we want to propagate through the parallel map.
                        if part == 2:
                            p_map[next_y][next_x] += p_map[y][x]

        # increase elevation, move onto the new spots to search
        elev += 1
        spots_to_search = new_spots_to_search
    
    # if this is part 1, we return how many 9's we were able to reach from that spot
    if part == 1:
        return len(spots_to_search)
    
    # if this is part 2, we add up the 9's values in the parallel map and then return the sum
    if part == 2:
        trail_ratings_sum = 0
        for y, line in enumerate(my_map):
            for x, n in enumerate(line):
                if n == 9:
                    trail_ratings_sum += p_map[y][x]
        return trail_ratings_sum


# for part 1, calculate the score for each trailhead individually, then add them up as you go
part_1 = 0
for start in starts:
    s = set()
    s.add(start)
    part_1 += trailblaze(s)

print(f"Part 1 solution: {part_1}")

print(f"Part 2 solution: {trailblaze(starts, 2)}")