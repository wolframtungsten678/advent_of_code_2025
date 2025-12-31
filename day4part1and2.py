pallet_raw = []
pallet = []
counter = 0
grid_state = True

with open('day4input.txt', 'r') as file:
    for row in file: 
        pallet_raw.append(row.strip())

# "." and "@" recoded to usable values
for row in pallet_raw: 
    row_1 = row.replace(".", "0")
    row_1 = row_1.replace("@", "1")
    pallet.append(row_1)

# Calculate number of rolls initially in grid
initial_rolls = 0
for row in pallet: 
    initial_rolls += row.count("1")

# Value retrieval and roll removal functions
def fetch_TLD(pallet, row, column):
    return int(pallet[row - 1][column - 1])

def fetch_TM(pallet, row, column):
    return int(pallet[row - 1][column])

def fetch_TRD(pallet, row, column):
    return int(pallet[row - 1][column + 1])

def fetch_L(pallet, row, column):
    return int(pallet[row][column - 1])

def fetch_R(pallet, row, column):
    return int(pallet[row][column + 1])

def fetch_BLD(pallet, row, column):
    return int(pallet[row + 1][column - 1])

def fetch_BM(pallet, row, column):
    return int(pallet[row + 1][column])

def fetch_BRD(pallet, row, column): 
    return int(pallet[row + 1][column + 1])

def remove_rolls(pallet, grid_remove):
    for row, column in grid_remove:
        pallet[row] = pallet[row][:column] + "0" + pallet[row][(column+1):]
    return None

# Begin interative checking if rolls can be removed
k = 0 # Enables printing of original number of rolls accessible for removal and not afterwards
while (grid_state == True): 
    grid_remove = []

    # Loop through paper grid & determine adjacent_total
    i = 0
    while i < 138:
        j = 0
        while j < 138:
            # Skip slot if empty and increment to next slot
            if (pallet[i][j] == "0"):
                j += 1
            else: 
                match i:
                    case 0:
                        match j:
                            case 0:
                                adjacent_total = fetch_R(pallet, i, j) + fetch_BRD(pallet, i, j) + fetch_BM(pallet, i, j)
                            case 137: 
                                adjacent_total = fetch_L(pallet, i, j) + fetch_BLD(pallet, i, j) + fetch_BM(pallet, i, j)
                            case _:
                                adjacent_total = fetch_L(pallet, i, j) + fetch_R(pallet, i, j) + fetch_BLD(pallet, i, j) + fetch_BM(pallet, i, j) + fetch_BRD(pallet, i, j)
                    case 137:
                        match j: 
                            case 0: 
                                adjacent_total = fetch_TM(pallet, i, j) + fetch_TRD(pallet, i, j) + fetch_R(pallet, i, j)
                            case 137: 
                                adjacent_total = fetch_TLD(pallet, i, j) + fetch_TM(pallet, i, j) + fetch_L(pallet, i, j)
                            case _:
                                adjacent_total = fetch_L(pallet, i, j) + fetch_R(pallet, i, j) + fetch_TLD(pallet, i, j) + fetch_TM(pallet, i, j) + fetch_TRD(pallet, i, j)
                    case _:
                        match j: 
                            case 0: 
                                adjacent_total = fetch_TM(pallet, i, j) + fetch_TRD(pallet, i, j) + fetch_R(pallet, i, j) + fetch_BRD(pallet, i, j) + fetch_BM(pallet, i, j)
                            case 137: 
                                adjacent_total = fetch_TM(pallet, i, j) + fetch_TLD(pallet, i, j) + fetch_L(pallet, i, j) + fetch_BLD(pallet, i, j) + fetch_BM(pallet, i, j)
                            case _:
                                adjacent_total = fetch_TLD(pallet, i, j) + fetch_TM(pallet, i, j) + fetch_TRD(pallet, i, j) + fetch_L(pallet, i, j) + fetch_R(pallet, i, j) + fetch_BLD(pallet, i, j) + fetch_BM(pallet, i, j) + fetch_BRD(pallet, i, j)
                
                if (adjacent_total < 4):
                    counter += 1
                    grid_remove.append([i,j])
                
                j += 1
        i += 1

    while k < 1: 
        print("Rolls of Paper Accessible in Original Grid: " + str(counter))
        k += 1
    
    # check if any rolls can be removed, and if so, remove them
    if (len(grid_remove) == 0):
        grid_state = False
    else: 
        remove_rolls(pallet, grid_remove)

    grid_remove.clear()

final_rolls = 0
for row in pallet: 
    final_rolls += row.count("1")

print("Total Number of Rolls Removed: " + str(initial_rolls - final_rolls))
