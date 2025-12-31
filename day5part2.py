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

# Seed array with first range
all_fresh_ranges.append([int(split_fresh_range[0][0]), int(split_fresh_range[0][1])])

for pair in split_fresh_range:
    match_found = False
    value_to_check_1 = int(pair[0])
    value_to_check_2 = int(pair[1])
    
    i = 0
    v1_match = []
    v2_match = []
    range_consumed = [] # Identifies if range fully encompasses another range 
    while i < len(all_fresh_ranges):
        range_lower_limit = int(all_fresh_ranges[i][0])
        range_upper_limit = int(all_fresh_ranges[i][1])
        between_limits_v1 = (value_to_check_1 >= range_lower_limit) and (value_to_check_1 <= range_upper_limit)
        between_limits_v2 = (value_to_check_2 >= range_lower_limit) and (value_to_check_2 <= range_upper_limit)
        
        # Both in range
        if (between_limits_v1 and between_limits_v2): 
            match_found = True
        # Lower value is out of range
        elif (value_to_check_1 < range_lower_limit) and between_limits_v2:
            match_found = True
            v2_match.append(i)
        # Upper value is out of range
        elif (value_to_check_2 > range_upper_limit) and between_limits_v1:
            match_found = True
            v1_match.append(i)
        # Range being checked is fully encompassed by pair
        elif (value_to_check_1 < range_lower_limit) and (value_to_check_2 > range_upper_limit):
            match_found = True
            range_consumed.append(i)
        # Full range out of range
        elif (value_to_check_1 > range_upper_limit) or (value_to_check_2 < range_lower_limit):
            i += 1
            continue
        i += 1
    if match_found == False: 
        all_fresh_ranges.append([value_to_check_1, value_to_check_2])
    elif match_found == True: 
        if len(v1_match) > 0:
            v1_index = v1_match[0]
        if len(v2_match) > 0: 
            v2_index = v2_match[0]
        
        if (len(v1_match) == 1) and (len(v2_match) == 1):
            v1_min = all_fresh_ranges[v1_index][0]
            v1_max = all_fresh_ranges[v1_index][1]
            v2_min = all_fresh_ranges[v2_index][0]
            v2_max = all_fresh_ranges[v2_index][1]
            # Determine minimum of new range
            if v1_min <= v2_min:
                new_range_min = v1_min
            else: 
                new_range_min = v2_min
            # Determine maximum of new range
            if v1_max >= v2_max: 
                new_range_max = v1_max
            else: 
                new_range_max = v2_max
            # Replace range 1 with new range and delete range 2
            all_fresh_ranges[v1_index] = [new_range_min, new_range_max]
            del all_fresh_ranges[v2_index]
        elif (len(v1_match) == 1) and (len(v2_match) == 0):
            all_fresh_ranges[v1_index] = [all_fresh_ranges[v1_index][0], value_to_check_2]
        elif (len(v1_match) == 0) and (len(v2_match) == 1):
            all_fresh_ranges[v2_index] = [value_to_check_1, all_fresh_ranges[v2_index][1]]
    
        # Remove any ranges fully encompassed by other ranges
        if len(range_consumed) != 0: 
            if (len(v1_match) > 0) or (len(v2_match) > 0):
                for value in range_consumed:
                    del all_fresh_ranges[value]
            else:
                all_fresh_ranges.append([value_to_check_1, value_to_check_2])
                for value in range_consumed:
                    del all_fresh_ranges[value]
    
    v1_match.clear()
    v2_match.clear()

for element in all_fresh_ranges:
    print(element)   

#calculate total
total = 0
for tuple in all_fresh_ranges: 
    total += (tuple[1]-tuple[0]+1)

print("Fresh Ingredient ID's: " + str(total))