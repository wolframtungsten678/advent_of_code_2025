import math
import numpy as np
import gc

junction_boxes = []

with open('day8input.txt', 'r') as file: 
    for row in file: 
        stripped_row = row.strip()
        junction_boxes.append(stripped_row.split(","))

# Calculate distances
distances = []
i = 0 # i is index of point 1 in junction_boxes
while i < (len(junction_boxes)-1):
    j = i + 1 # j is index of point 2 in junction_boxes
    while j < len(junction_boxes):
        x1 = int(junction_boxes[i][0])
        x2 = int(junction_boxes[j][0])
        y1 = int(junction_boxes[i][1])
        y2 = int(junction_boxes[j][1])
        z1 = int(junction_boxes[i][2])
        z2 = int(junction_boxes[j][2])
        
        distance = math.sqrt(((x2-x1)**2)+((y2-y1)**2)+((z2-z1)**2))
        distance_element = (distance, i, j)
        distances.append(distance_element)

        j += 1
    
    i += 1

# Determine sorted indices
sorted_distance_indices = []
sorted_distance_indices = np.argsort([d[0] for d in distances])

# Create array of circuits
circuits = []

# Populate circuits array with first distance
point_1 = distances[sorted_distance_indices[0]][1]
point_2 = distances[sorted_distance_indices[0]][2]
circuits.append([point_1, point_2])

k = 1
while k < 1000: 
    distance_index = sorted_distance_indices[k]
    point_1_index = distances[distance_index][1]
    point_2_index = distances[distance_index][2]

    # Add point 1 or point 2 to a circuit as appropriate
    found_1 = False
    found_2 = False
    point_1_circuit = -1
    point_2_circuit = -1

    l = 0
    while l < len(circuits): 
        point_1_found = point_1_index in circuits[l]
        if point_1_found:
            found_1 = True
            point_1_circuit = l
        
        point_2_found = point_2_index in circuits[l]
        if point_2_found: 
            found_2 = True
            point_2_circuit = l
        
        l += 1

    if found_1 and (not found_2): 
        circuits[point_1_circuit].append(point_2_index)
    elif found_2 and (not found_1):
        circuits[point_2_circuit].append(point_1_index)
    elif found_1 and found_2: 
        if point_1_circuit != point_2_circuit: 
            circuit_to_move = circuits[point_2_circuit]
            circuits[point_1_circuit].extend(circuits[point_2_circuit])
            del circuits[point_2_circuit]
    else: 
        circuits.append([point_1_index, point_2_index])

    k += 1

# Find 3 largest circuits
circuits_sizes = []
for circuit in circuits:
    circuits_sizes.append(len(circuit))

sorted_circuits_sizes = []
sorted_circuits_sizes = np.argsort(circuits_sizes)

max_index = len(sorted_circuits_sizes) - 1

circuit_1_index = sorted_circuits_sizes[max_index]
circuit_2_index = sorted_circuits_sizes[max_index - 1]
circuit_3_index = sorted_circuits_sizes[max_index - 2]

total = circuits_sizes[circuit_1_index] * circuits_sizes[circuit_2_index] * circuits_sizes[circuit_3_index]

print(total)

gc.collect()