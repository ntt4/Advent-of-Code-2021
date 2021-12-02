## Day Two.One: Dive
## forward X increases the horizontal position by X units.
## down X increases the depth by X units.
## up X decreases the depth by X units.
## Note that since you're on a submarine, down and up affect your depth, and so they have the opposite result of what you might expect.

# Your horizontal position and depth both start at 0. The steps above would then modify them as follows:

# forward 5 adds 5 to your horizontal position, a total of 5.
# down 5 adds 5 to your depth, resulting in a value of 5.
# forward 8 adds 8 to your horizontal position, a total of 13.
# up 3 decreases your depth by 3, resulting in a value of 2.
# down 8 adds 8 to your depth, resulting in a value of 10.
# forward 2 adds 2 to your horizontal position, a total of 15.
# After following these instructions, you would have a horizontal position of 15 and a depth of 10. (Multiplying these together produces 150.)

# Calculate the horizontal position and depth you would have after following the planned course. What do you get if you multiply your final horizontal position by your final depth?

## Import aoctools to get the input from aoc
from aoctools import inputs
aoc_data = inputs(2,2021)
input_raw = aoc_data.get_input()
## You have to split lines here, else when it is called in the loop further down in prints each character individually
input = input_raw.splitlines()

## Input comes in as text but will need to be split so we cna handle the string and int's.
## Attempting to use .split(' ') to break the string value from the int/string onto a new online
# input_split = input_raw.splitlines()
# print(input_split)
## This works but doesn't split to lines as expected .split gives wonky output and .splitlines only splits on /n, is it possible to assign these to variables in a for loop?

## Enumerate doesn't work here. Can't copy from yesterday since we really don't need to have an index for any good reason
# for index, value in enumerate(input_split):
#     print(index, value)

## Set the variables that are to be used (These are given to us within the problem statement)
depth = 0
horizontal = 0

## Now that the input has a movement and a value on the same line, since it breaks if you don't do .splitlines(), we can unpack both of the values within a for loop
## Each line goes through the loop, two variables are set per iteration. movement and value. These are generated by splitting each line at the whitespace between the
## movement word and the int value. It's like making a table, but without CSV :L 
for eachline in input:
    movement, value = eachline.split(' ',1)

    ## Make if statements to check each of the movements and add the approrpiate value to the appropriate variable
    # if movement == 'forward':
    #     horizontal += 1
    ## I made a mistake here, we're not conuting this time, so we don't add 1. We add the value to the var instead, like so...
    
    ## Remember than 'value' is being returned as a string thanks to .split, so we need to tell Python to use an int instead
    if movement == 'forward':
        horizontal += int(value)
    elif movement == 'down':
        depth += int(value)
    elif movement == 'up':
        depth -= int(value)
print(horizontal*depth)
