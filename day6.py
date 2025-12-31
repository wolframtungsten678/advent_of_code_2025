raw_cephalopod_math = []

with open('day6input.txt', 'r') as file:
    for row in file: 
        raw_cephalopod_math.append(row.split())

print(raw_cephalopod_math)

total = 0
i = 0
while i < len(raw_cephalopod_math[0]):
    value_1 = int(raw_cephalopod_math[0][i])
    value_2 = int(raw_cephalopod_math[1][i])
    value_3 = int(raw_cephalopod_math[2][i])
    value_4 = int(raw_cephalopod_math[3][i])
    operation = raw_cephalopod_math[4][i]
    
    if operation == "+":
        total += (value_1+value_2+value_3+value_4)
    elif operation == "*":
        total += (value_1*value_2*value_3*value_4)
    else: 
        print("Error -- invalid operation")
        break

    i += 1

print("Total :" + str(total))