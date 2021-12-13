## Day Three.One: Binary Diagnostics
## The submarine has been making some odd creaking noises, so you ask it to produce a diagnostic report just in case.
## The diagnostic report (your puzzle input) consists of a list of binary numbers which, when decoded properly, can tell you many useful things about the conditions of the submarine. 
## The first parameter to check is the power consumption.

## You need to use the binary numbers in the diagnostic report to generate two new binary numbers (called the gamma rate and the epsilon rate). 
## The power consumption can then be found by multiplying the gamma rate by the epsilon rate.

## Each bit in the gamma rate can be determined by finding the most common bit in the corresponding position of all numbers in the diagnostic report. 
## For example, given the following diagnostic report:

## 00100
## 11110
## 10110
## 10111
## 10101
## 01111
## 00111
## 11100
## 10000
## 11001
## 00010
## 01010

## Considering only the first bit of each number, there are five 0 bits and seven 1 bits. Since the most common bit is 1, the first bit of the gamma rate is 1.
## The most common second bit of the numbers in the diagnostic report is 0, so the second bit of the gamma rate is 0.
## The most common value of the third, fourth, and fifth bits are 1, 1, and 0, respectively, and so the final three bits of the gamma rate are 110.
## So, the gamma rate is the binary number 10110, or 22 in decimal.

## The epsilon rate is calculated in a similar way; rather than use the most common bit, the least common bit from each position is used. 
## So, the epsilon rate is 01001, or 9 in decimal. Multiplying the gamma rate (22) by the epsilon rate (9) produces the power consumption, 198.
## Use the binary numbers in your diagnostic report to calculate the gamma rate and epsilon rate, then multiply them together. 

## What is the power consumption of the submarine? (Be sure to represent your answer in decimal, not binary.)

## Bootstrap
from collections import Counter
from aoctools import inputs
aoc_data = inputs(3,2021)
## input_raw got replaced with input as I realised you can do .splitlines on a method in a variable, neat
input = aoc_data.get_input().splitlines
# input_raw = aoc_data.get_input()

## Checking to see if we can see how long each binary value is, doing the below returns the total number of lines in the file, not the length of a line
# test = len(input_raw)

## Test if we got the input we expected by printing it
# print(input_raw)

## The variables below are given to us in the problem statement above
power_consumption = 0
## As I found out much much later, these two need to be strings, not ints
gamma_rate = epsilon_rate = ""


## Get input data
## Get expected length of binary value
## Check if it is correct, else throw an expection

## If correct then we have options; 
## Enumerate through it with a for loop and do some jazz, I don't know what this jazz entails though
## Can we count how many times a number appears
## Create a ind dictionary for each binary value and use indecies to count the values
## Convert to a base 2 int and unpack the value, some how, maybe? Is it possible to count the bits this way?

## Then print it back and check the result / add error code
## Personally, I like the bottommost idea... but it seems like a crazy way of doing it... 🙃

## Then mess with the values till we get a result we can do stuff with

## These wouldn't work but I wanted to test. 
# for eachline in input_raw.splitlines():
#     pass

# for index, value in enumerate(input_raw.splitlines()):
#     print(index)

## Using len we can check the length of the bits we have in the input. Unlike when I tried above, I realised you can use an index to reference a specific line

# print(type(input()))
# len_of_0_idx = len(input()[0])
# print(len_of_0_idx)

## Python has a nice library called 'collections' which has a module called 'counter', it literally counts how many times something occurs.
## Trouble is, how can we check the position of those values? Or... do we actually need to do that at all and only count the 0's and 1's??
## Testing counter below. Creating a var with Counter as the class and setting the input to the first value from the input
## Printing the value, to confirm, and then using .most_common(1) to get the result of the most common value within that input and printing it
# c = Counter(input()[0])
# print(input()[0])
# ## most_common returns a list, []
# most_common = c.most_common(1)
# print(most_common)

## input() is a list and when using a list, you can call the index and the character by using [line_idx] [string_idx]
# b = input()[1][1]
# print(b)

## Could we then cycle through these, we know the length of the bit using len?
## binary and binarylength variables maybe?

## We only need to work out the most common bit/binary number, as the least common is just the value inverted?
# most_common = None

## Convert the binary to base2 and save the ints in a list, is this handy at all? Probably not.
## Me from the later on in the day... Turns out it was, I can use this to flip the binary values to base2 to make the final value up!
# int_list = [int(value, 2) for value in input()]
## We can use max() to find the longest value in the input and use that as our binary length, assuming that all values will be the same
## Maybe throw an ValueError if not?
max_binary_length = max(len(binary) for binary in input())

# c = Counter(input()[0])
# most_common = c.most_common()
## c.most_common() returns a list. Is it possible to iterate through it and use an index to get the values?
# print(type(most_common))
## You can, you can use an index [] to get the results back from the list! 
## The below returns...
## [('1', 7), ('0', 5)]
## [('1', 7)]
## [('1', 7), ('0', 5)]
# print(c.most_common())
# print(c.most_common(1))
# print(c.most_common(2))
## So we can index to get values, we know that 'c.most_common(1)[0][0]' is going to return the most common value and it's count
## Then we can do 'c.most_common()', to get all values and do append [-1][0[0] to get the least common, as [-1] returns the last value


## I've just realised that the above doesn't help at all, since we're still only acting upon one number and not the column 😞

## Attempting to make a list of all the data per column, doesn't work either. It just returns the memory address of each bit of data
# column_list = []
# for eachline in input_raw:
#     column_list.append(eachvalue[eachline] for eachvalue in input_raw)


## Ok, back to counter. Is there a way we can slice the data so that if checks the value in each idx position and iterates through it?
## I'm going to bash this out and see if my logic sticks, because why not >.<
# for value in range[0:max_binary_length]:
#     c = Counter(input()[value])
#     most_common = c.most_common(1)[0][0]
#     least_common = c.most_common()[-1][0][0]
    ## We can't do the above as it still only works on one entire binary input, not a column / slice. Is there a way to generate this?

# ## Create a for loop so that we cycle through each value from idx 0 to the max_binary_length
# ## I was using a : here for the longest of time instead of a ','. range uses a , to set the range!
# ## ... I was also using [] instead of (). It's late and I'm tired 🥱
# ## Remeber too, instead of using 'value' or 'eachline' that Python has some formatting. l for line, i for int, etc
# for i in range(0,max_binary_length):
#     ## If the above does what I think it does, it will print numbers 0 through 11
#     # print(i)
#     ## It did, now, is it possible to generate a list by creating a loop that goes through all the values in idx 0, then idx 1, idx 2, etc?
#     ## This, should, look at input() for data, get the value in the index, as we're iterating through the for loop, and then add it to the list
#     bit_list = [value[i] for value in input()]
#     ## It did, but only for all the characters in idx0... darn
#     ## oh no wait, it get's overwritten each time! I was only seeing the last run each time as I was doing the print outside of the loop. Durr
#     #print(bit_list)
#     ## IT'S WORKING!!!!
#     c = Counter(bit_list)
#     ## Doing c.most_common and then the indexing trick from above works, but doesn't scale well if this gets built out. Is there a better way? It'll do for now
#     # most_common = c.most_common(1)[0][1]
#     # least_common = c.most_common()[-1][1]
#     ## Add the value of most_common to gamma and the value of least_common to epsilon
#     gamma_rate += most_common
#     epsilon_rate += least_common
# ## So the above for loop spits out 6139, 5861. This is the count of each digit in each column, not a binary representation as expected...
# # print(gamma_rate)
# # print(epsilon_rate)

####
## I did something wrong above as it was returning the count of the digits in each idx rather than the most common and least common digit.
## Easily fixed by changing the index that c.most_common looked up to 0, or so I thought! 
## Thankfully, Python threw me a bone. TypeError: unsupported operand type(s) for +=: 'int' and 'str'
## Looks like I need to set the variables where these get added to, 'gamma_rate' and 'epsilon_rate' to strings!
for i in range(0,max_binary_length):

    bit_list = [value[i] for value in input()]
    c = Counter(bit_list)
    ## Flipping the index to [0] to return the actual number rather than the count of numbers
    most_common = c.most_common(1)[0][0]
    least_common = c.most_common()[-1][0]
    gamma_rate += most_common
    epsilon_rate += least_common
## Now it returns a binary, as expected. Time to convert it and wrap up!
gamma_int = int(gamma_rate,2)
epsilon_int = int(epsilon_rate,2)
print(f'Answer: {gamma_int*epsilon_int}')