node_list = []
stack = []
paths = 0

class Node: 
    def __init__(self, device, connections):
        self.device = device
        self.connections = connections
        self.visited_connections = [False] * len(connections)

    def copy_node(self):
        return Node(self.device, self.connections)

    def print_node(self):
        print("Device name: " + str(self.device))
        print("Connections: " + str(self.connections))
        print("Visited Status: " + str(self.visited_connections))
        

# Load input file
with open('day11input.txt', 'r') as file:
    for row in file: 
        stripped_row = row.strip()
        split_row = stripped_row.split(": ")
        raw_connections = split_row[1].split(" ")
        
        # Create Node and add to node list
        new_node = Node(split_row[0], raw_connections)
        node_list.append(new_node)

# Sort node list by device name and create dictionary to quickly find nodes
sorted_node_list = sorted(node_list, key=lambda x: x.device)
node_dict = {}
i = 0
while i < len(sorted_node_list):
    device_name = sorted_node_list[i].device
    node_dict[device_name] = i
    i += 1

# Begin graph traversal
starting_point_index = node_dict['you']
stack.append(sorted_node_list[starting_point_index])
while len(stack) > 0: 
    active_node = stack[-1]  
    
    # If all paths already visited, pop from stack
    all_visited = [True] * len(active_node.connections)
    node_status = active_node.visited_connections
    if (all_visited == node_status):
        j = 0
        while j < len(active_node.visited_connections):
            active_node.visited_connections[j] = False
            j += 1            
        stack.pop()
        continue

    # Loop through connections of active node and follow paths not yet visited
    i = 0 
    while i < len(active_node.connections):
        # Increment i if current connection is already visited
        if (active_node.visited_connections[i] == True): 
            i += 1
        # Add connection to stack if path not visited, or increment path if 
        # connection is 'out'
        if active_node.visited_connections[i] == False: 
            active_node.visited_connections[i] = True
            node_to_add = active_node.connections[i]
            if node_to_add != 'out':
                node_to_add_index = node_dict[node_to_add]
                stack.append(sorted_node_list[node_to_add_index])
                break
            else: # If node is 'out', path end is reached, no node appended
                paths += 1
                i += 1
                
print("Total paths: " + str(paths))    