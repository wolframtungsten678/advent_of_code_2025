import numpy as np

input_data = []

# Class definitions
class Tree():
    def __init__(self, length, width, gift_index):
        self.length = length
        self.width = width
        self.area = length * width
        self.array = [[0] * width for _ in range(length)]
        self.gift_index = gift_index

class Gift():
    def __init__(self, type_index):
        self.tl_corner = (0,0)
        self.type = type_index
        self.config = gift_configs[type_index]
        self.rotation = rotations[type_index]
        self.reflect = reflec_symm[type_index]
        self.working_config = self.config

# Function definitions
## Reflects gift configuration
def reflect_gift(gift, total_num_rotations, tree):
    gift_config = gift.config
    transposed = np.transpose(gift_config)
    gift.working_config = transposed
    try_to_place = gift_placement(gift, tree) 

    if try_to_place == True: 
        return True
    else: 
        rotate_gift(gift, total_num_rotations, tree)
        return rotate_gift(gift, total_num_rotations, tree)


## Rotates gift configuration and returns whether valid placement found
def rotate_gift(gift, total_num_rotations, tree):
    rot = 0
    while rot < total_num_rotations:
        transposed = np.transpose(gift.working_config)
        reversed_rows = np.flipud(transposed)
        gift_config = reversed_rows
        gift.working_config = gift_config
        try_to_place = gift_placement(gift, tree)
        if try_to_place == False:
            rot += 1
        else: 
            break
    
    return try_to_place

## Updates gift.tl_corner to next tree grid placement for gift and returns 
## whether valid placement can be found
def gift_placement(gift, tree):
    can_be_placed = False
    at_final_spot = (gift.tl_corner[1] == tree.width - 3) and (gift.tl_corner[0] == tree.length - 3)
    while (can_be_placed == False) and (at_final_spot == False): 
        if gift.tl_corner[1] < (tree.width - 3):
            gift.tl_corner = (gift.tl_corner[0], gift.tl_corner[1] + 1)
        elif gift.tl_corner[0] < (tree.length - 3):
            gift.tl_corner = (gift.tl_corner[0] + 1, 0)
        
        can_be_placed = placement_possible(gift, tree)
        if can_be_placed == True: 
            break
        else: 
            at_final_spot = (gift.tl_corner[1] == tree.width - 3) and (gift.tl_corner[0] == tree.length - 3)
            if at_final_spot == True:
                gift.tl_corner = (0,0)
                return False
    return can_be_placed

## Evaluates if gift can be placed at current gift.tl_corner
def placement_possible(gift, tree):
    can_place = True
    if (gift.tl_corner[0] + 3 > tree.length or gift.tl_corner[1] + 3 > tree.width):
        return False
        
    initial_tl_corner_row = gift.tl_corner[0]
    initial_tl_corner_column = gift.tl_corner[1]
    row = gift.tl_corner[0]
    while row < gift.tl_corner[0] + 3:
        column = gift.tl_corner[1]
        while column < gift.tl_corner[1] + 3:
            gift_row_index = row - initial_tl_corner_row
            gift_column_index = column - initial_tl_corner_column
            gift_config_value = gift.working_config[gift_row_index][gift_column_index]
            tree_array_value = tree.array[row][column]
            if (gift_config_value + tree_array_value) > 1:
                can_place = False
                return can_place
            column += 1
        row += 1
    return can_place

## Places gift in available location
def place_gift(gift_stack, tree):    
    ### Place a gift in array at location specified and pop gift from stack
    row = 0
    while row < 3:
        column = 0
        while column < 3:
            tree_row = gift_stack[-1].tl_corner[0]+row
            tree_column = gift_stack[-1].tl_corner[1]+column
            tree_array = tree.array
            tree_array[tree_row][tree_column] = gift_stack[-1].working_config[row][column]
            column += 1
        
        row += 1
    gift_stack.pop()
        
    ### Base case
    if len(gift_stack) == 0:
        return 1
    else: 
        can_place_gift = False
        while can_place_gift == False:
            ### Find next spot/arrangement to place gift
            can_place_gift = gift_placement(gift_stack[-1], tree)
            ### Check if placement is acceptable
            if can_place_gift == True:
                ### Recurse with new placement
                return place_gift(gift_stack, tree)
            else: 
                ### Rotate and reflect gift until placement found
                can_place_gift = rotate_gift(gift_stack[-1], gift_stack[-1].rotation, tree)
                if can_place_gift == False:
                    if gift_stack[-1].reflect == True:
                        gift_stack[-1].working_config = gift_stack[-1].config
                        can_place_gift = reflect_gift(gift_stack[-1], gift_stack[-1].rotation, tree)
                        if can_place_gift == False: 
                            return 0
                        else: 
                            return place_gift(gift_stack, tree)
                    else: 
                        return 0
                else: 
                    ### Recurse with new placement
                    return place_gift(gift_stack, tree)
                
                
        
# Extract input file
with open('day12input.txt', 'r') as file:
    for line in file: 
        current_line = line.strip()
        if current_line == "":
            continue
        else: 
            input_data.append(current_line)

gift_configs = []
gift_sizes = []
trees = []

input_data_length = len(input_data)
i = 0
while i < input_data_length:
    if len(input_data[i]) == 2: 
        # Convert gift configuration to arrays of 0's and 1's
        gift_row_1 = input_data[i+1].translate(str.maketrans({"." : "0", "#" : "1"}))
        gift_row_2 = input_data[i+2].translate(str.maketrans({"." : "0", "#" : "1"}))
        gift_row_3 = input_data[i+3].translate(str.maketrans({"." : "0", "#" : "1"}))
        gift_row_1_split = [int(gift_row_1[0]),int(gift_row_1[1]), int(gift_row_1[2])]
        gift_row_2_split = [int(gift_row_2[0]),int(gift_row_2[1]), int(gift_row_2[2])]
        gift_row_3_split = [int(gift_row_3[0]),int(gift_row_3[1]), int(gift_row_3[2])]
        gift_configs.append([gift_row_1_split, gift_row_2_split, gift_row_3_split])
        # Calculate area gift occupies
        gift_size = gift_row_1.count('1')+gift_row_2.count('1')+gift_row_3.count('1')
        gift_sizes.append(gift_size)

        i += 4
    else: 
        parsed_tree = input_data[i].split(": ")
        area = parsed_tree[0].split("x")
        gift_quants = parsed_tree[1].split(" ")
        new_tree = Tree(int(area[0]), int(area[1]), gift_quants)
        trees.append(new_tree)
        i += 1

# Document number of rotations needed, and if reflection symmetric for gift types
rotations = [3,3,3,3,1,3]
reflec_symm = [True, False, True, True, True, False]

trees_to_test = []

# Create list of trees that require testing
for tree in trees: 
    tree_area = tree.area
    total_gift_area = 0
    i = 0
    while i < len(gift_sizes):
        total_gift_area += int(tree.gift_index[i])*gift_sizes[i]
        i += 1

    if total_gift_area > tree_area:
        continue
    else: 
        trees_to_test.append(tree)

# Loop through trees in trees_to_test 
tree_count = 0
for tree in trees_to_test: 
    # Populate gift stack
    gift_stack = []
    j = 0
    while j < len(tree.gift_index):
        num_gifts = int(tree.gift_index[j])
        k = 0
        while k < num_gifts:
            new_gift = Gift(j)
            gift_stack.append(new_gift)
            k += 1
        j += 1
    # Place gifts in tree area
    tree_count += place_gift(gift_stack, tree)
    print(tree_count)

    gift_stack.clear()

print("Tree Count: " + str(tree_count))