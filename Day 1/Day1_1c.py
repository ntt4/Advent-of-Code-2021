from aoctools import inputs
aoc_data = inputs(1,2021)
input_raw = aoc_data.get_input()
input = aoc_data.convert_to_int_array(text=input_raw)

increased_count = 0
for index, value in enumerate(input):
    if index == 0:
        continue
    if value > input[index -1]:
        increased_count += 1

print("result1")
print(increased_count)