fresh_range = []

with open('day5input.txt', 'r') as file:
    for row in file:
        if row.count("-") == 1:
            fresh_range.append(row.strip())
        else: 
            continue

split_fresh_range = []

for element in fresh_range: 
    split_fresh_range.append(element.split("-"))

all_fresh_ranges = []

#seed array with first range
all_fresh_ranges.append((int(split_fresh_range[0][0]), int(split_fresh_range[0][1])))

for pair in split_fresh_range:
    match_found = False
    value_to_check_1 = int(pair[0])
    value_to_check_2 = int(pair[1])
    
    i = 0
    while i < len(all_fresh_ranges):
        range_lower_limit = int(all_fresh_ranges[i][0])
        range_upper_limit = int(all_fresh_ranges[i][1])
        between_limits_v1 = (value_to_check_1 >= range_lower_limit) and (value_to_check_1 <= range_upper_limit)
        between_limits_v2 = (value_to_check_2 >= range_lower_limit) and (value_to_check_2 <= range_upper_limit)
        
        if (between_limits_v1 and between_limits_v2): 
            match_found = True
        elif (value_to_check_1 < range_lower_limit) and between_limits_v2:
            all_fresh_ranges[i] = (value_to_check_1, all_fresh_ranges[i][1])
            match_found = True
        elif (value_to_check_2 > range_upper_limit) and between_limits_v1:
            all_fresh_ranges[i] = (all_fresh_ranges[i][0], value_to_check_2)
            match_found = True
        elif (value_to_check_1 > range_upper_limit) or (value_to_check_2 < range_lower_limit):
            i += 1
            continue
        i += 1
    if match_found == False: 
        all_fresh_ranges.append((value_to_check_1, value_to_check_2))
    

#calculate total
total = 0
for tuple in all_fresh_ranges: 
    total += (tuple[1]-tuple[0]+1)

print(total)