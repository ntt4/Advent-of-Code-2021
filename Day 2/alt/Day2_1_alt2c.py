from aoctools import inputs
aoc_data = inputs(2,2021)
input_raw = aoc_data.get_input()
depth = horizontal = 0

def format_to_ind_dict(input_data):
    split_input = input_data.split(' ',1)
    if len(split_input) != 2:
        raise Exception('split_input contains an incorrect number of values')
    try:
        return {
            'movement':split_input[0],
            'value':int(split_input[1])
        }
    except:
        raise Exception('Unable to add key:value from a correctly formatted split_input to the dictionary')

dict_comprehension = [format_to_ind_dict(eachline) for eachline in input_raw.splitlines()]

for eachdict in dict_comprehension:
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