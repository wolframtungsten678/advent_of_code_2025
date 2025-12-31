import csv
import builtins

def pattern_check(string) -> int:
    string_length = len(string)
    for i in builtins.range(1, string_length):
        test_string = string[:i]
        if test_string * (len(string) // len(test_string)) == string:
            return 1
    return 0


raw_data = []

with open("day2input.txt", "r") as file: 
    reader = csv.reader(file)

    for line in reader: 
        raw_data.append(line)

barcode_ranges = []
counter = 0

for range in raw_data[0]:
    parsed_list = range.split("-")
    barcode_ranges.append(parsed_list)

for element in barcode_ranges: 
    range_start = int(element[0])
    range_end = int(element[1])
    temp_array = []

    while range_start <= range_end:
        temp_array.append(range_start)
        range_start += 1

    for number in temp_array: 
        number_string = str(number)
        multiplier = pattern_check(number_string)
        counter += number * multiplier

print("New Rules - Invalid ID's: " + str(counter))
