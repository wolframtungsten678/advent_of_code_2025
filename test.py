pallet_raw = []
pallet = []

with open('day4testinput.txt', 'r') as file:
    for row in file: 
        pallet_raw.append(row.strip())

# "." and "@" recoded to usable values
for row in pallet_raw: 
    row_1 = row.replace(".", "0")
    row_1 = row_1.replace("@", "1")
    pallet.append(row_1)

initial_rolls = 0
for row in pallet: 
    initial_rolls += row.count("1")

print(initial_rolls)