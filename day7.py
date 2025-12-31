tachyon_manifold = []
split_count = 0

with open('day7input.txt', 'r') as file: 
    for row in file: 
        tachyon_manifold.append(row.strip())

row = 0
while row < len(tachyon_manifold):
    column = 0
    while column < len(tachyon_manifold[0]):
        current_symbol = tachyon_manifold[row][column]
        current_row = tachyon_manifold[row]
        if row != 0:
            previous_row = tachyon_manifold[row - 1]
        
        if current_symbol == "S":
            next_row = tachyon_manifold[row + 1]
            tachyon_manifold[row +1] = next_row[:column] + "|" + next_row[column + 1:]
        elif current_symbol == ".":
            if row != 0: 
                if previous_row[column] == "|":
                    tachyon_manifold[row] = current_row[:column] + "|" + current_row[column + 1:]
        elif current_symbol == "^":
            if previous_row[column] == "|":
                tachyon_manifold[row] = current_row[:column - 1] + "|^|" + current_row[column + 2:]
                split_count += 1
        column += 1
    row += 1

print("Beam Split Count: " + str(split_count))