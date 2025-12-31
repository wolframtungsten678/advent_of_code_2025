import csv
import builtins

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
        temp_array.append(str(range_start))
        range_start += 1

    for number in temp_array: 
        if ((len(number)%2) == 0):
            number_half = len(number)// 2
            if number[:number_half] == number[number_half:]:
                counter += int(number)

print("Invalid ID's: " + str(counter))