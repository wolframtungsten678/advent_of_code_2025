battery_banks = []

with open('day3input.txt', 'r') as file:
    for line in file: 
        battery_banks.append(line.strip())

total_joltage = 0

for bank in battery_banks: 
    digit_1 = max(bank[:(len(bank)-1)])
    digit_2_search = bank.find(digit_1) + 1
    digit_2 = max(bank[digit_2_search:])
    joltage = digit_1 + digit_2
    total_joltage += int(joltage)

print(total_joltage)