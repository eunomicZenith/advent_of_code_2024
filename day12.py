from copy import deepcopy

with open(r'inputs\day12.txt') as input_file:
    raw_input = input_file.readlines()
my_garden = [list(line.rstrip('\n')) for line in raw_input]

height = len(my_garden)
width = len(my_garden[0])
dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)]
c_garden = deepcopy(my_garden)
total_cost = 0
discounted_cost = 0

for j, row in enumerate(c_garden):
    for k, plot in enumerate(row):
        if plot != '.':
            
            # time to search for neighbors yay
            coords_to_search = set()
            coords_to_search.add((j, k))
            group_coords = set()
            group_coords.add((j, k))
            while coords_to_search:
                new_coords_to_search = set()
                
                # for each starting spot, check its neighbors...
                for spot in coords_to_search:
                    y, x = spot
                    for dir in dirs:
                        dy, dx = dir
                        next_y, next_x = y + dy, x + dx
                        
                        # avoid stepping outside the map
                        if 0 <= next_x < width and 0 <= next_y < height:
                            neighbor = c_garden[next_y][next_x]
                            
                            # check if the neighbor is the same; if so, search it next, and add it to the group
                            if neighbor == plot and (next_y, next_x) not in group_coords:
                                new_coords_to_search.add((next_y, next_x))
                                group_coords.add((next_y, next_x))
                coords_to_search = new_coords_to_search
            
            perimeter = 0
            area = len(group_coords)
            edges = set()
            
            # go through each plot in the group we've found
            for c in group_coords:
                y, x = c
                # this destroys plots we've already counted, to prevent double-counting
                c_garden[y][x] = '.'
                # check all four plots around it
                for dir in dirs:
                    dy, dx = dir
                    next_y, next_x = y + dy, x + dx
                    # if that direction doesn't have a plot that's part of the group, add 1 to perimeter
                    # and also add that spot (and the direction you're looking from) to the "edges" set, for part 2
                    if (next_y, next_x) not in group_coords:
                        perimeter += 1
                        edges.add((next_y, next_x, dir))
            total_cost += area * perimeter
            
            while edges:
                # grab any edge
                edge_1 = edges.pop()
                # "side" is the set of contiguous edges that form a side
                side = set()
                side.add(edge_1)
                y1, x1, dir1 = edge_1
                # check all directions; one or two may find adjacent edges, the others don't matter
                for dir_e in dirs:
                    # just keep going in that direction, until you *don't* find an adjacent edge
                    mult = 1
                    while True:
                        dy, dx = dir_e
                        y1n, x1n = y1 + (dy*mult), x1 + (dx*mult)
                        # when you find an adjacent edge, add it to the side, then increase mult to check if the next is too
                        if (y1n, x1n, dir1) in edges:
                            side.add((y1n, x1n, dir1))
                            mult +=1
                        # if there's no edge after that, we're done with this direction
                        else:
                            break
                discounted_cost += area
                # getting rid of the edges we've just finished counting
                for edge in side:
                    edges.discard(edge)

print(total_cost)
print(discounted_cost)