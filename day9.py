red_tiles = []
rectangle_areas = []

with open('day9input.txt', 'r') as file: 
    for row in file:
        stripped_row = row.strip()
        red_tiles.append(stripped_row.split(","))

i = 0
while i < len(red_tiles) - 1:
    j = i + 1
    while j < len(red_tiles): 
        tile_1_x = int(red_tiles[i][0])
        tile_2_x = int(red_tiles[j][0])
        tile_1_y = int(red_tiles[i][1])
        tile_2_y = int(red_tiles[j][1])
        area = abs(1 + tile_1_x - tile_2_x) * abs(1 + tile_1_y - tile_2_y)
        rectangle_areas.append(area)
        j += 1
    i += 1

largest_rectangle = max(rectangle_areas)

print("Largest Rectangle Area: " + str(largest_rectangle))