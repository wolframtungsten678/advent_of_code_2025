tachyon_manifold = []
nodes = []
timelines = 0

with open('day7input.txt', 'r') as file: 
    for row in file: 
        tachyon_manifold.append(row.strip())

total_rows = len(tachyon_manifold)
total_columns = len(tachyon_manifold[0])
tachyon_manifold = []
nodes = []
timelines = 0

with open('day7input.txt', 'r') as file: 
    for row in file: 
        tachyon_manifold.append(row.strip())

total_rows = len(tachyon_manifold)
total_columns = len(tachyon_manifold[0])

# Node Class
class Node:
    def __init__(self, row, column):
        self.row = row
        self.column = column
        self.p1 = column - 1
        self.p2 = column + 1
        self.p1_visited = False
        self.p2_visited = False
    
    # Function to check if node can be popped from stack
    def node_check(self):
        if self.p1_visited and self.p2_visited: 
            value = "None"
        elif self.p1_visited and not self.p2_visited: 
            value = "p2"
        elif self.p2_visited and not self.p1_visited: 
            value = "p1"
        elif not self.p1_visited and not self.p2_visited: 
            value = "Both"
        
        return value
    
    def print_node(self):
        print("[" + str(self.row) + " , " + str(self.column) + "], " + str(self.p1_visited) + ", " + str(self.p2_visited))


# Function to find next node and append to nodes array. Returns whether node was appended
def find_next(node, path, array, node_list):
    row = node.row
    column = path
    node_added = False
    next_node = next((x for x in node_list if (x[0] > row and x[1] == column)), None)
    if next_node != None:
        node_added = True
        new_node = Node(next_node[0], next_node[1])
        array.append(new_node)
    
    return node_added

# Create array of all nodes 
node_list = []
i = 0
while i < total_columns:
    j = 0
    while j < total_rows:
        current_symbol = tachyon_manifold[j][i]
        if current_symbol == "^":
            node_list.append([j,i])
        j += 1
    i += 1

# Identify column to begin search
beam_start_column = -1
row = 0
while row < total_rows:
    column = 0
    while beam_start_column == -1:
        current_symbol = tachyon_manifold[row][column]
        if current_symbol == "S":
            beam_start_column = column
        column += 1
    row += 1

#Identify first node
row = 0
while row < total_rows:
    if tachyon_manifold[row][beam_start_column] == "^":
        node_1 = Node(row, beam_start_column)
        nodes.append(node_1)
        break
    row += 1

while len(nodes) > 0: 
    current_node = nodes[-1]
    check = current_node.node_check()
    if check == "None":
        #current_node.p1_visited = False
        #current_node.p2_visited = False
        nodes.pop()
        continue
    elif (check == "p1") or (check == "Both"):
        nodes[-1].p1_visited = True
        if not find_next(current_node, current_node.p1, nodes, node_list): 
            timelines += 1
            continue
    elif check == "p2":
        nodes[-1].p2_visited = True
        if not find_next(current_node, current_node.p2, nodes, node_list):
            timelines += 1
            continue
    



print(timelines)  