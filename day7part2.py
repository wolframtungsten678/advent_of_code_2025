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
    p1_visited = False
    p2_visited = False

    def visit_p1(self):
        self.p1_visited = True

    def visit_p2(self):
        self.p2_visited = True
    
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


# Function to find next node
def find_next(node, path):
    row = node.row
    node_added = False
    while row < total_rows - 1:
        next_row = row + 1
        if tachyon_manifold[next_row][path] == "^":
            new_node = Node(row, path)
            nodes.append(new_node)
            node_added = True
            break
        row += 1
    
    return node_added

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
    check = nodes[-1].node_check()
    if check == "None":
        nodes.pop()
    elif check == "p2":
        nodes[-1].visit_p2()
        if not find_next(nodes[-1], nodes[-1].p2):
            timelines += 1
    elif check == "p1" or "Both":
        nodes[-1].visit_p1()
        if not find_next(nodes[-1], nodes[-1].p1): 
            timelines += 1
    nodes[-1].print_node()

print(timelines)    