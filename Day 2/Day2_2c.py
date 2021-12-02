from aoctools import inputs
aoc_data = inputs(2,2021)
input_raw = aoc_data.get_input()
input = input_raw.splitlines()

aim = 0
depth = 0
horizontal = 0

for eachline in input:
    movement, value = eachline.split(' ',1)
    if movement == 'forward':
        horizontal += int(value)
        depth += (aim*int(value))
    elif movement == 'down':
        aim += int(value)
    elif movement == 'up':
        aim -= int(value)
print(depth)
print(horizontal)
print(horizontal*depth)
