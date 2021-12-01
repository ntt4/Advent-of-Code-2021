from aoctools import inputs
aoc_data = inputs(1,2021)
input_raw = aoc_data.get_input()
input = aoc_data.convert_to_int_array(text=input_raw)

current_value = 0
previous_value = 0
increased_count = 0

for index, value in enumerate(input):
    previous_value = current_value
    slice = input[index:index+3]
    current_value = sum(slice)
    if previous_value == 0:
        continue
    if current_value > previous_value:
        increased_count +=1
print(increased_count)