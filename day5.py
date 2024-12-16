with open(r'inputs\day5.txt') as input_file:
    raw_input = input_file.readlines()
input_strings = [line.rstrip('\n') for line in raw_input]

updates = []
rules = set()

for line in input_strings:
    if "|" in line:
        rules.add(tuple(line.split("|")))
    if "," in line:
        updates.append(line.split(","))


def is_valid_update(my_prios):
    for idx1, id1 in enumerate(my_prios):
        for id2 in my_prios[idx1 + 1:]:
            if (id2, id1) in rules:
                return False
    return True


answer_1 = 0
for update in updates:
    if is_valid_update(update):
        answer_1 += int(update[int((len(update) - 1) / 2)])
print("Answer 1:", answer_1)


# part 2


def fix_update(update):
    new_update = []
    my_update = update.copy()
    while my_update:
        i = 0
        u = my_update[i]
        found = False
        while not found:
            found = True
            for u2 in my_update:
                if (u2, u) in rules:
                    i += 1
                    u = my_update[i]
                    found = False
                    break
        smallest_u = my_update.pop(i)
        new_update.append(smallest_u)
    return new_update


answer_2 = 0
for update in updates:
    if not is_valid_update(update):
        fixed_update = fix_update(update)
        answer_2 += int(fixed_update[int((len(update) - 1) / 2)])
print("Answer 2:", answer_2)