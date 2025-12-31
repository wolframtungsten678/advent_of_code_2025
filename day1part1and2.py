instructions = []

with open('day1input.txt', 'r') as file:
    for line in file: 
        instructions.append(line.strip())

counter = 0
land_zero = 0
dial = 50
dial_size = 100

for string in instructions:
    direction = string[0]
    turn_value = int(string[1:])
    
    if direction == "R":
        pass_zero = (dial + turn_value) // dial_size
        dial = (dial + turn_value) % dial_size
        if dial == 0: 
            land_zero += 1
        
    elif direction == "L":
        if dial == 0: 
            pass_zero = turn_value // dial_size
        elif turn_value >= dial: 
            pass_zero = 1 + ((turn_value - dial) // dial_size)
        else: 
            pass_zero = 0
        dial = (dial - turn_value) % dial_size
        if dial == 0: 
            land_zero += 1

                    
    counter += pass_zero

print("Land on zero: " + str(land_zero))
print("Pass zero and land on zero: " + str(counter))