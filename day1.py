import math

instructions = []

with open('day1input.txt', 'r') as file:
    for line in file: 
        instructions.append(line.strip())

counter = 0
dial = 50
dial_size = 100

for string in instructions:
    direction = string[0]
    turn_value = int(string[1:])
    
    if direction == "L":
        pass_zero = math.floor(((dial_size - dial) + turn_value) / dial_size)
        dial = (dial - turn_value) % dial_size
        
    else:
        pass_zero = math.floor((dial + turn_value) / dial_size)
        dial = (dial + turn_value) % dial_size
                    
    counter = counter + pass_zero

print(counter)