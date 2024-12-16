from collections import defaultdict

with open(r'inputs\day11.txt') as input_file:
    raw_input = input_file.read().rstrip('\n')
starting_stones = raw_input.split(" ")

# this is a dict, where each key is a type of stone and its value is the number of stones of that type
my_stones = defaultdict(lambda: 0)
for stone in starting_stones:
    my_stones[stone] += 1


def stoneliferator(stones, blinks_target):
    blinks = 0
    
    # we will keep looping until we run out of blinks to do
    while blinks < blinks_target:
        
        # make an empty dict for the next generation of stones
        new_stones = defaultdict(lambda: 0)
        
        # for each type of stone, we add an equivalent amount of the relevant stones to the next generation
        for stone in stones:
            stone_amount = stones[stone]
            if stone == "0":
                new_stones["1"] += stone_amount
            elif len(stone) % 2 == 0:
                new_stones[str(int(stone[:len(stone)//2]))] += stone_amount
                new_stones[str(int(stone[len(stone)//2:]))] += stone_amount
            else:
                new_stones[str(int(stone) * 2024)] += stone_amount
        
        # end of the generation, the new stones become current ones, increment the blinks
        stones = new_stones
        blinks += 1
    
    # once we're done blinking, let's count all the stones
    total_stones = 0
    for stone in stones:
        stone_amount = stones[stone]
        total_stones += stone_amount
    return total_stones


print(f"Stones after 25 blinks: {stoneliferator(my_stones, 25)}")
print(f"Stones after 75 blinks: {stoneliferator(my_stones, 75)}")