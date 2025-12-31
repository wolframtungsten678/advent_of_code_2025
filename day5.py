fresh_range = []
ingredient_list = []
counter = 0

with open('day5input.txt', 'r') as file:
    for row in file: 
        if row.count("-") == 1:
            fresh_range.append(row.strip())
        elif row.strip() == "": 
            continue
        else: 
            ingredient_list.append(int(row.strip()))

split_fresh_range = []

for element in fresh_range: 
    split_fresh_range.append(element.split("-"))

for ingredient in ingredient_list:
    for value in split_fresh_range:
        if ((ingredient >= int(value[0])) and (ingredient <= int(value[1]))):
            counter += 1
            break

print("Fresh Ingredient ID's: " + str(counter))