# THIS IS A WIP - OPTIMIZATION FOR SPEED IS NEEDED
## Functions well for small data set in day9testinput.txt

from collections import defaultdict

def boundary_check(tile_1, tile_2, direction):
    if direction == "x": 
        y_values = [tile_1[0], tile_2[0]]
        for row in y_values:
            if tile_1[1] > tile_2[1]:
                lower_limit = tile_2[1]
                upper_limit = tile_1[1] + 1
            elif tile_1[1] == tile_2[1]:
                lower_limit = tile_1[1]
                upper_limit = tile_1[1] + 1
            else: 
                lower_limit = tile_1[1]
                upper_limit = tile_2[1] + 1
            # Check if each point in the horizontal boundaries of the rectangle is in a range in
            # boundary_rows or boundary_columns; If not, check for boundaries above, below, left
            # and right of the point 
            for point in range(lower_limit, upper_limit, 1):
                range_found = False
                for col_range in boundary_rows.get(row): 
                    if point >= col_range[0] and point <= col_range[1]:
                        range_found = True
                        break
                    else: 
                        continue
                if range_found == False:                  
                    range_below = False
                    # Check row numbers below for boundary
                    for value in range(row):
                        if boundary_rows.get(value) == None:
                            continue
                        for col_range_2 in boundary_rows.get(value):
                            if point >= col_range_2[0] and point <= col_range_2[1]:
                                range_below = True
                                break
                            else: 
                                continue
                        if range_below == True: 
                            break
                    
                    range_above = False
                    # Check row numbers above for boundary
                    for value in range(row + 1, total_rows + 1, 1):
                        if boundary_rows.get(value) == None:
                            continue
                        for col_range_3 in boundary_rows.get(value):
                            if point >= col_range_3[0] and point <= col_range_3[1]:
                                range_above = True
                                break
                            else: 
                                continue
                        if range_above == True: 
                            break

                    # Check if a valid range in boundary_columns encompasses the point
                    if range_below == False and range_above == False: 
                        if boundary_columns.get(point) == None: 
                            continue
                        for row_range in boundary_columns.get(point):
                            if row >= row_range[0] and row <= row_range[1]:
                                range_found = True
                                break
                            else: 
                                continue
                    elif range_below == True and range_above == True: 
                        range_found = True
                            
                # If a point has been found that is not in any range, break out of the loop early
                if range_found == False: 
                    return False
    elif direction == "y": 
        x_values = [tile_1[1], tile_2[1]]
        for column in x_values:
            if tile_1[0] > tile_2[0]:
                lower_limit_y = tile_2[0]
                upper_limit_y = tile_1[0] + 1
            elif tile_1[0] == tile_2[0]:
                lower_limit_y = tile_1[0]
                upper_limit_y = tile_1[0] + 1
            else: 
                lower_limit_y = tile_1[0]
                upper_limit_y = tile_2[0] + 1
            for point in range(lower_limit_y, upper_limit_y, 1):
                range_found = False
                for row_range in boundary_columns.get(column): 
                    if point >= row_range[0] and point <= row_range[1]:
                        range_found = True
                        break
                    else: 
                        continue
                if range_found == False:                  
                    range_left = False
                    # Check columns to left for boundary
                    for value in range(column):
                        if boundary_columns.get(value) == None: 
                            continue
                        for row_range_2 in boundary_columns.get(value):
                            if point >= row_range_2[0] and point <= row_range_2[1]:
                                range_left = True
                                break
                            else: 
                                continue
                        if range_left == True: 
                            break
                    
                    range_right = False
                    # Check columns to right for boundary
                    for value in range(column + 1, total_columns + 1, 1):
                        if boundary_columns.get(value) == None: 
                            continue
                        for row_range_3 in boundary_columns.get(value):
                            if point >= row_range_3[0] and point <= row_range_3[1]:
                                range_right = True
                                break
                            else: 
                                continue
                        if range_right == True: 
                            break

                    # Check if a valid range in boundary_columns encompasses the point
                    if range_left == False and range_right == False: 
                        if boundary_rows.get(point) == None: 
                            continue
                        for col_range in boundary_rows.get(point):
                            if column >= col_range[0] and column <= col_range[1]:
                                range_found = True
                                break
                            else: 
                                continue
                    elif range_left == True and range_right == True: 
                        range_found = True
                            
                # If a point has been found that is not in any range, break out of the loop early
                if range_found == False: 
                    return False             
    return True


red_tiles = []
boundary_rows = defaultdict(list)
boundary_columns = defaultdict(list)
rectangle_areas = []
total_rows = 0
total_columns = 0
largest_rectangle_area = 0

with open('day9input.txt', 'r') as file: 
    for row in file:
        stripped_row = row.strip()
        point_pairs = stripped_row.split(",")
        red_tiles.append([int(point_pairs[0]), int(point_pairs[1])])

# Generate dictionary of ranges of green tiles by row and column, and establish total number of rows and
# columns in point grid
i = 0
while i < len(red_tiles):
    point_1 = red_tiles[i]
    
    # loop to first element at end of red_tiles
    if i != len(red_tiles) - 1: 
        point_2 = red_tiles[i + 1]
    else: 
        point_2 = red_tiles[0]

    if point_1[0] == point_2[0]: 
        if point_1[1] > point_2[1]:
            boundary_rows[point_1[0]].append((point_2[1], point_1[1]))
            if point_1[1] >= total_columns:
                total_columns = point_1[1]
        else: 
            boundary_rows[point_1[0]].append((point_1[1], point_2[1]))
            if point_2[1] >= total_columns:
                total_columns = point_2[1]
    else: 
        if point_1[0] > point_2[0]:
            boundary_columns[point_1[1]].append((point_2[0], point_1[0]))
            if point_1[0] >= total_rows:
                total_rows = point_1[0]
        else: 
            boundary_columns[point_1[1]].append((point_1[0], point_2[0]))
            if point_2[0] >= total_rows:
                total_rows = point_2[0]
    i += 1

# Find areas of all possible rectangles with red tiles at opposite corners
areas_evaluated = 0
for tile in range(len(red_tiles)):
    for next_tile in range(tile + 1, len(red_tiles), 1): 
        tile_1 = red_tiles[tile]
        tile_2 = red_tiles[next_tile]
        
        # Find area of the rectangle 
        tile_1_x = red_tiles[tile][0]
        tile_2_x = red_tiles[next_tile][0]
        tile_1_y = red_tiles[tile][1]
        tile_2_y = red_tiles[next_tile][1]
        area = (1 + abs(tile_1_x - tile_2_x)) * (1 + abs(tile_1_y - tile_2_y)) 
        
        # If rectangle area is larger than current max, check if rectangle boundaries are in 
        # green tile range     
        if area > largest_rectangle_area:
            y_bounds = boundary_check(tile_1, tile_2, "y")
            x_bounds = boundary_check(tile_1, tile_2, "x")
            if x_bounds and y_bounds:   
                largest_rectangle_area = area

        areas_evaluated += 1
        if areas_evaluated % 10 == 0:
            print("Areas Evaluted: " + str(areas_evaluated))



print("Largest Rectangle Area: " + str(largest_rectangle_area))
