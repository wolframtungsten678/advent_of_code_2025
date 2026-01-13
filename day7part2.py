# THIS IS A WIP - OPTIMIZATION FOR SPEED IS NEEDED

from collections import defaultdict
from bisect import bisect_right

tachyon_manifold = []
nodes = []
timelines = 0

with open('day7input.txt', 'r') as file: 
    for row in file: 
        tachyon_manifold.append(row.strip())

total_rows = len(tachyon_manifold)
total_columns = len(tachyon_manifold[0])

# Create dictionary of all nodes and identify column to begin search
all_nodes = defaultdict(list)
for row in range(total_rows):
    for col in range(total_columns):
        current_symbol = tachyon_manifold[row][col]
        if current_symbol == "^":
            all_nodes[col].append(row)
        elif current_symbol == "S":
            beam_start_column = col

# Sort nodes in each column by increasing row 
for col in all_nodes:
    all_nodes[col].sort()

#Identify first node
first_node_row = None
for row in all_nodes[beam_start_column]:
    first_node_row = row
    node_1 = [row, beam_start_column, False, False] # Node format is [row, column, left, right]
    nodes.append(node_1)
    break

# Find next node in path and add to stack until end of tachyon_manifold is reached, then step backwards 
# to find additional paths 
while len(nodes) > 0: 
    if timelines % 1000000 == 0:
        print(timelines)
    current_node = nodes[-1]
    if nodes[-1][2] == True and nodes[-1][3] == True:
        nodes.pop()
        continue
    elif current_node[2] == False:
        nodes[-1][2] = True
        search_column = current_node[1] - 1
        rows = all_nodes.get(search_column, False)
        if rows == False:
            timelines += 1
            continue
        next_node_index = bisect_right(rows, current_node[0])
        if next_node_index < len(rows):
            nodes.append([rows[next_node_index], search_column, False, False])
        else: 
            timelines += 1
            continue
    elif current_node[3] == False:
        nodes[-1][3] = True
        search_column = current_node[1] + 1
        rows = all_nodes.get(search_column, False)
        if rows == False:
            timelines += 1
            continue
        next_node_index = bisect_right(rows, current_node[0])
        if next_node_index < len(rows):
            nodes.append([rows[next_node_index], search_column, False, False])
        else: 
            timelines += 1
            continue
    
  
print("Total timelines: " + str(timelines))