from aoctools import inputs
aoc_data = inputs(2,2021)
input_raw = aoc_data.get_input()
## If you use .split() without any arguments, it automatically splits on whitespace and newlines
## This would work for the inital way I was dealing with this and the majority of the for loops below
## but when it comes to using the for loop in use, it worked to splitlines() here instead so that
## the raw input returned full lines rather than a pre-split list of a individial characters
# input = input_raw.split()
## You don't even need to do this, in the for loop below, it has the method called upon it inline
# input = input_raw.splitlines()


## If you are delcaring a variable with the same value as another, you can do it all in one line. Neat!
depth = horizontal = 0

## Attempting to use Python 3.10.0's pattern matching 
## For the most part, it works like an if statement, but it's more efficient as it doesn't need to check each statement
## However, it doesn't appear as though you can do 'movement, value = eachline.split('',1)' within the loop
## How do we do this outside of the loop instead? Do that split outside and somehow create an index, like with enumerate?

## This is what I expected to work, but you can't do the line split and then a match. You'd have to generate an array or a dict outside
## of the for sttement and then pass the values into each case
# for eachline in input:
#     movement, value = eachline.split('',1)
#     match movement:
#         case 'forward':
#             print('forward')
#         case 'up':
#             print('up')
#         case 'down':
#             print('down')

## Create an array or dictionary using the input to store the two values?
## You can use [x] to return a specific index from a .split(). So is it posssible to use that to itterate through the input
## and generate an array?
# movement = input[0]
# value = input[1]

# index_one = 0
# index_two = 1

# storage = dict()

## This for loop doesn't work because you're not indexing the data from input but from each item :/
# for item in input:
#     movement = input[index_one]
#     value = input[index_two]
#     storage[movement] = value
#     index_one += 2
#     index_two += 2
# print (storage)


## The two for loops below work fine and return the same result, but a dict is not the right way to store this data
# for item in input_splitlines:
#      movement, value = item.split(' ',1)
#      storage[movement] = movement
#      storage[value] = value
# print(storage)

# for eachline in input:
#     movement, value = eachline.split(' ',1)
#     storage[movement] = movement
#     storage[value] = value
# print(storage)

## () brackets are for tuples, [] are for lists! 
# dict_list = ()

## What we're doing below is pretty neat...
## dict_list is a var that stores a list of each individual dictionary entry containting the movement and value values
## from the for loop below it

## Create a new list var that will hold the output of the for loop below
dict_list = []

## This for loop iterates through each line from the input_raw data
for eachline in input_raw.splitlines():
    ## For each iteration of the loop, it gets the line value, eg 'forward 6', then uses .split() to split the line at
    ## the whitespace. The first value 'forward' gets assigned to 'movement' while the second value '6' gets assigned to value
    movement, value = eachline.split(' ',1)
    ## Create a dictionary with the movement and value variables assigned to their specific keys
    ## Be sure to set the type here too so that we don't run into trouble later
    dict = {'movement':str(movement),'value':int(value)}
    ## Append the above dictionary to the dict_list variable, doing this means that each line has it's own dictionary that we
    ## can then iterate through later using pattern matching.
    ## If eachline is not added as it's own dict and instead gets added into one dict it does not work, as we can't have duplicate
    ## results in a dictionary and also can't match them later!
    dict_list.append(dict)

## This for loop inerates through each dict in the dict_list created above
for eachdict in dict_list:
    ## For eachdict we check the 'movement' key and see if it matches any of the cases below. If it does, we jump to that case
    ## and act upon it directly, instead of cycling through things as if we were using an 'if' or 'elif' statement
    match eachdict['movement']:
        ## For example, here we check to see if the value of the key 'movement' is 'foward'. If it is and the case matches
        ## we add the value from the iterated dictionary and add it too the 'horizontal' variable
        ## Since we set the types earlier when creating the dict, we don't have to worry about type conversion here
        case 'forward':
            horizontal += eachdict['value']
        case 'up':
            depth -= eachdict['value']
        case 'down':
            depth += eachdict['value']
        ## Delcaring _ as a case allows us to catch things if there is some value that we can't handle
        case _:
            raise Exception(f'Unable to handle movement {eachdict["movement"]}')
## And we're done!
print(horizontal*depth)