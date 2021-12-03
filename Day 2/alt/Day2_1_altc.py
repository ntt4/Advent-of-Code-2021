from aoctools import inputs
aoc_data = inputs(2,2021)
input_raw = aoc_data.get_input()
depth = horizontal = 0

dict_list = []

for eachline in input_raw.splitlines():
    movement, value = eachline.split(' ',1)
    dict = {'movement':str(movement),'value':int(value)}
    dict_list.append(dict)

for eachdict in dict_list:
    match eachdict['movement']:
        case 'forward':
            horizontal += eachdict['value']
        case 'up':
            depth -= eachdict['value']
        case 'down':
            depth += eachdict['value']
        case _:
            raise Exception(f'Unable to handle movement {eachdict["movement"]}')
print(horizontal*depth)