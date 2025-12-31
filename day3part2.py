battery_banks = []

with open('day3input.txt', 'r') as file:
    for line in file: 
        battery_banks.append(line.strip())

total_joltage = 0

for bank in battery_banks: 
    current_slice_end = len(bank) - 11
    digit_1 = max(bank[:current_slice_end])
    joltage = digit_1
    current_slice_start = bank.find(digit_1) + 1
    i = 11
    while i > 0: 
        current_slice_end += 1
        next_digit = max(bank[current_slice_start:current_slice_end])
        joltage += next_digit
        
        print(bank[current_slice_start:current_slice_end].find(next_digit))
        current_slice_start += bank[current_slice_start:current_slice_end].find(next_digit) + 1
        i -= 1
   
    print(joltage)
    total_joltage += int(joltage)

print("Total Joltage: " + str(total_joltage))