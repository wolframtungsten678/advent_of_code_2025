raw_cephalopod_math = []

with open('day6input.txt', 'r') as file:
    for row in file: 
        raw_cephalopod_math.append(row)

# Determine which space is delimiter and replace with a comma
i = 0
end_index = len(raw_cephalopod_math[0]) - 1
while i < end_index:
    symbol = raw_cephalopod_math[4][i]

    if (symbol == "+") or (symbol == "*"):
        raw_cephalopod_math[0] = raw_cephalopod_math[0][:(i-1)] + "," + raw_cephalopod_math[0][i:end_index]
        raw_cephalopod_math[1] = raw_cephalopod_math[1][:(i-1)] + "," + raw_cephalopod_math[1][i:end_index]
        raw_cephalopod_math[2] = raw_cephalopod_math[2][:(i-1)] + "," + raw_cephalopod_math[2][i:end_index]
        raw_cephalopod_math[3] = raw_cephalopod_math[3][:(i-1)] + "," + raw_cephalopod_math[3][i:end_index]
        raw_cephalopod_math[4] = raw_cephalopod_math[4][:(i-1)] + "," + raw_cephalopod_math[4][i:end_index]
    i += 1


# Split into separate strings based on the delimiter
parsed_cephalopod_math = []
j = 0
while j < len(raw_cephalopod_math):
    parsed_cephalopod_math.append(raw_cephalopod_math[j].split(","))
    j += 1

print(parsed_cephalopod_math)

# Calculate total value
total = 0
k = 0
while k < len(parsed_cephalopod_math[0]):
    size = len(parsed_cephalopod_math[0][k])
    symbol = parsed_cephalopod_math[4][k]
    val_1_init = parsed_cephalopod_math[0][k][0]
    val_2_init = parsed_cephalopod_math[1][k][0]
    val_3_init = parsed_cephalopod_math[2][k][0]
    val_4_init = parsed_cephalopod_math[3][k][0]
    subtotal = int(val_1_init + val_2_init + val_3_init + val_4_init)
    
    l = 1
    while l < size: 
        val_1_subs = parsed_cephalopod_math[0][k][l]
        val_2_subs = parsed_cephalopod_math[1][k][l]
        val_3_subs = parsed_cephalopod_math[2][k][l]
        val_4_subs = parsed_cephalopod_math[3][k][l]
        if symbol.strip() == "*":
            subtotal *= int(val_1_subs + val_2_subs + val_3_subs + val_4_subs)
        elif symbol.strip() == "+":
            subtotal += int(val_1_subs + val_2_subs + val_3_subs + val_4_subs)
        l += 1

    total += subtotal
    k += 1

print("Total :" + str(total))