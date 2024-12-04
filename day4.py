import regex as re

with open(r'inputs\day4.txt') as input_file:
    raw_input = input_file.readlines()
puz_input = [line.rstrip('\n') for line in raw_input]

# flips the puz_input across its diagonal axis ("transposes", apparently)
def zip_flip(wordsearch):
    return ["".join(n) for n in zip(*wordsearch)]

# skews the array so that you get strings from all the diagonals
def skew_array(wordsearch):
    array = wordsearch.copy()
    for n in range(len(array)):
        array[n] = ('.' * n) + array[n] + ('.' * (len(array) - n))
    return zip_flip(array)

# counts how many xmas (and samx) in each row, including overlapping ones (thanks unofficial regex)
def count_xmas(wordsearch):
    count = 0
    for line in wordsearch:
        instances = re.findall(r"XMAS|SAMX", line, overlapped=True)
        count += len(instances)
    return count

# reverses the array left-to-right, which is useful to search the other diagonals
def reverse(wordsearch):
    return [n[::-1] for n in wordsearch]

# let's count all the xmas/samx in horizontal, vertical, upward diagonal and downward diagonal
part_1_count = sum(
    [count_xmas(puz_input),
    count_xmas(zip_flip(puz_input)),
    count_xmas(skew_array(puz_input)),
    count_xmas(skew_array(reverse(puz_input)))]
)

print(f"Number of XMAS: {part_1_count}")

# part 2

def count_cross_mas(wordsearch):
    count = 0
    array = skew_array(wordsearch)
    
    # we're going to search for MAS/SAM in the diagonals. one direction of diagonals suffices
    for y in range(len(array)):
        iters = re.finditer(r"MAS|SAM", array[y], overlapped=True)
        
        # for each MAS/SAM we find, we check if it's part of a X-MAS
        for instance in iters:
            x = instance.start()+1
            
            # this part was tricky: in the skew board, the cell that's "diagonal" is two up/down and one left/right
            # now I know, and it makes sense once you see it graphically
            up = array[y-2][x-1]
            down = array[y+2][x+1]
            if up+down == "MS" or up+down == "SM":
                count +=1
    return count

print(f"Number of X-MAS: {count_cross_mas(puz_input)}")