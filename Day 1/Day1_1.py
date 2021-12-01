#Day One.One - Sonar Sweep


## x for x in in z if x > previousvalue 
# #if current value has increased then add to count 

# Import CSV
# import csv

# # #Load the values file, read only, via 'with open' and assign it to a variable
## Nope, this is just bad xD Let's not deal with CSV's, please.
# with open('./values.csv','r') as loadedValues:
#     #Create CSV reader
#     loadedValuesReader = csv.reader(loadedValues)
#     for value in loadedValuesReader:
#         if value 

from aoctools import inputs
aoc_data = inputs(1,2021)
input_raw = aoc_data.get_input()
input = aoc_data.convert_to_int_array(text=input_raw)

## This works but feels like a hack if we ever go over 99999999
## It also ignores the first value if it were lower, I think...
## Is it possible to get python to reference itself or add a lookup to the data?
# increased_count = 0
# previous_value = 99999999
# for value in input:
#     if value > previous_value:
#         increased_count +=1
#     previous_value = value
# print(increased_count)

## You can get specific values directly from the array if you add the index value in
# print(input[2])
## Can't use index() as it finds the first result, which wouldn't work for duplicates... darn

## Enumerate is neat as it adds as index to the data we are dealing with and means I don't have
## to do anything hacky like...
# index = 0            # Python's indexing starts at zero
# for item in items:   # Python's for loops are a "for each" loop 
#     print(index, item)
#     index += 1

increased_count = 0
for index, value in enumerate(input):
    ## Check if we're on the first entry in the enumerated array as we have nothing to compare it to... skip!
    if index == 0:
        continue
    ## Check if the value is greater than the previous value from the input using the index and negating one entry
    if value > input[index -1]:
        increased_count += 1

print("result1")
print(increased_count)