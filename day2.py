from numpy import sign

with open(r'inputs\day2.txt') as input_file:
    raw_input = input_file.readlines()
input_strings = [line.rstrip('\n') for line in raw_input]

# split the input into reports made of levels
u_data = [[int(lev) for lev in report.split()] for report in input_strings]

safe_count = 0
safe_ish_count = 0

# this function checks if a report is safe
def safe_check(report):
    
    # use the difference between the first two levels to establish increasing/decreasing. They should ALL be the same as this one!
    trend = sign(report[0] - report[1])
    
    # go through the levels pairwise (0-1, 1-2, etc.) and compute their difference.
    for i in range(len(report)-1):
        diff = report[i] - report[i+1]
        
        # three fail conditions: wrong increase/decrease, or diff too low, or diff too high
        if sign(diff) != trend or abs(diff) < 1 or abs(diff) > 3:
            return False
    
    # if nothing went wrong, return True
    return True

for r in u_data:
    # check each report. If it's totally safe, increase both "safe" and "safeish" counters.
    if safe_check(r):
        safe_count += 1
        safe_ish_count += 1
    
    # if it's not totally safe, we're just going to check if it can *become safe* with one element removed
    # we do this by creating copies of the report with one element removed
    # and then we feed it to the safe_check function again
    # this is inefficient, brute-force, but each report only has 5 numbers, so it's not that bad
    # trying to code logic to figure out which level was the problem proved tricky
    # mostly because of the "all increasing/decreasing" requirement
    # and with this few levels it just wasn't worth doing
    else:
        for n in range(len(r)):
            r_cut = r.copy()
            r_cut.pop(n)
            
            # if any of the copies are safe, the report can be salvaged, so increment the "safeish" counter
            if safe_check(r_cut):
                safe_ish_count += 1
                break

print(f"Safe reports: {safe_count}")
print(f"Safe-ish reports: {safe_ish_count}")