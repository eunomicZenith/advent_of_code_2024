from collections import Counter

with open(r'inputs\day1.txt') as input_file:
    raw_input = input_file.readlines()
input_strings = [line.rstrip('\n') for line in raw_input]

# part 1

# make two lists, one for each column
# I initially did this with append (normally) before deciding I'd use zip for some reason
a_list, b_list = [[int(x) for x in a] for a in zip(*[line.split() for line in input_strings])]

# sort each list in increasing order, to ensure the pairs match up correctly
a_list.sort()
b_list.sort()

# tally up the absolute values of the differences between the right element and the left element
difsum = 0
for i in range(len(a_list)):
    difsum += abs(a_list[i] - b_list[i])

print(f"Part 1 solution: {difsum}")

# part 2

# create a dictionary that has the amount of times each number appears in column B
# this is overkill for the relatively small input given, probably, since 1000^2 is "only" 1 mil
# but I think doing this might decrease the big O notation?
# compared to just... counting how many elements in B are the same as every element in A, over and over, which is O(n^2)
# but maybe searching through the dictionary's keys is still bad for the big O notation? idk.
# depending on how "elem in frequencies" works, it might at least be less bad.

frequencies = Counter(b_list)

# "Counter" is a very neat class I found out about that's designed for EXACTLY this use scenario!!
# "defaultdict" also exists (allows to do stuff to not-yet-existent keys), which is also rather neat. but this is more specialized.
# initially I just checked if the entry exists, increment if it does, set to 1 if it doesn't yet.
# however, Counter was too neat to resist the temptation.

# once you have the dictionary of amounts in column B, just go through column A
# and multiply each number in A by the amount of times it appears in B, and add it all up to the sim_score.
sim_score = 0
for elem in a_list:
    if elem in frequencies:
        sim_score += elem * frequencies[elem]

print(f"Part 2 solution: {sim_score}")