#Day One.Two - Sonar Sweep

from aoctools import inputs
aoc_data = inputs(1,2021)
input_raw = aoc_data.get_input()
input = aoc_data.convert_to_int_array(text=input_raw)

## Three measurement sliding window
## Basically, get 0, then 1, then 2 so 0,1,2 then 1,2,3 then 2,3,4, then 3,4,5 etc
## I really have no idea what I'm doing :/ 
# calculate 3 sliding values at a time eg 012 + 123 + 234 and store in a var then 345 + 456 + 567 etc and store in a var
# then compare the vars against each other

## So calling if value > input[index :+3] doesn't work. Why? Because index is being returned as an int and not the actual array value
## How do you do this programmatically, you can't just do value1 + value2, etc
## Is there a way to take a slice of the array that is returned from enumerate and calculate the values / store them?
# for index, value in enumerate(input):
#     sliding1 = value? 
#     if value > input[index :-3]:
#         increased_count +=1

# print("result2")
# print(increased_count)


## The total of the current three numbers being calculated need to be stored and also the previous three numbers to compare, and the count!
## And other than that, I have no idea how to calculate it without taking chunks of the array, which Google Fu will help with!
current_value = 0
previous_value = 0
increased_count = 0

## Trying to test this by created a new object 'test=enumerate(inputs)' and printing(test[index:index+2]) fails due to it not being callable
# test = enumerate(input)
# print(test)
## However, this works if you do it in a for loop! So is it possible to pass the 'index' var and add 3? eg input([index:index+3])?? (YOU CAN!!!!!)
# for index, value in enumerate(input):
#     print(input[1:5])

for index, value in enumerate(input):
    # Store the previous'current' value as 'previous_value' when we go loop around
    previous_value = current_value
    ## Create a new var and slice the array. It should add three to the latter value each time it loops as the 'index' value automatically increments each loop
    ## Will it go out of bounds though once it reaches the end of the array? Apparently not, but why not? 🤔
    slice = input[index:index+3]
    ## Set the current value as the sum of the slice
    current_value = sum(slice)
    ## If the previous value == 0, assume we're getting started for the first time
    if previous_value == 0:
        continue
    if current_value > previous_value:
        increased_count +=1

print("result2")
print(increased_count)