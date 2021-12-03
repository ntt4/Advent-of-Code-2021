from aoctools import inputs

## Attempting to create a method to handle formatting the raw input to a dict
## Saves doing it in a for loop and means that it can be re-used and added to aoctools if needed
## This basically does the same as the for loop from the original. It...
## 1) Splits the string/line given to it
## 2) Saves that split line data within a variable as a list
## 3) Checks to see if there are anything other than two values in that list
## 4) Creates a dictionary from the values within the list that have been indexed via [x] and the returns this to the
##    list comphension variable in the main program 
def format_to_ind_dict(input_data):
    ## Take the input data that is passed through to the method and split it to a string, like we did in the for loop in the original
    ## attempt at the task
    ## Note that while we could do the following...
    # movement, value = input_data.split(' ',1)
    # print(movement)
    # print(value)
    ## ... it doesn't provide much flexibility. If we want to check that we had, at least some, values given to us for the key pair
    ## then we can add the split to a variable instead and then reference the content that we want using the index of the split eg...
    split_input = input_data.split(' ',1)
    # print(split_input[0])
    # print(split_input[1])
    ## This also enables exception checks, the potential to expand to further enteries if needed and to manipulate the data in a better
    ## way, all of which are something that I should be looking to improve on and not just creating the smallest program to complete a task
    ## eg, if len(split_length) is not equal to 2, then throw an exception, as we'd have more (or less) data than we can handle
    ## len(x) returns the number of items within a container, such as a list, tuple, etc
    if len(split_input) != 2:
        raise Exception('split_input contains an incorrect number of values')
    ## Python uses try / except (which is the same as try/catch in C#)
    ## Here we try to return a values back to the dict_comprehension variable, which should add them as a new dict each time the method
    ## is iterated upon. The 'except' should catch any errors if the data contains the correct number of inputs but is incorrectly formatted
    try:
        return {
            ## Here we create the values to be returned to the dictionary. {} define a dictionary. In this instance, a new dict will be created
            ## everytime we iterate through the method
            ## Here, we know that the first value, index0, is our movement value, it comes in as a string
            'movement':split_input[0],
            ## We also know that our second value, index1, is our integer value, so we can set the type using int(x)
            'value':int(split_input[1])
        }
    except:
        raise Exception('Unable to add key:value from a correctly formatted split_input to the dictionary')

aoc_data = inputs(2,2021)
input_raw = aoc_data.get_input()
depth = horizontal = 0


## Use a comprehension to pass the input data to the method
## The comprehension is wrapped in [] so that the results of the method are stored within a list
## This allows for multiple dicts to be stored which can then be iterated through when we use match
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