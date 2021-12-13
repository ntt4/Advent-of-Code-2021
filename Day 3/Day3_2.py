from collections import Counter
from aoctools import inputs
aoc_data = inputs(3,2021)
input = aoc_data.get_input().splitlines


## Switching up some variable names as I've realised that I've been using binary instead of bit
o2_rating = 0
co2_rating = 0

max_binary_length = max(len(binary) for binary in input())

for i in range(0,max_binary_length):
    bit_list = [value[i] for value in input()]
    c = Counter(bit_list)

    most_common = c.most_common(1)[0][0]
    least_common = c.most_common()[-1][0]

    gamma_rate += most_common
    epsilon_rate += least_common

gamma_int = int(gamma_rate,2)
epsilon_int = int(epsilon_rate,2)
print(f'Answer: {gamma_int*epsilon_int}')




life_rating = o2_rating * co2_rating

## Each rating has a bit criteria
## We start on the first bit in each column and discard numbers that do not match
## If there is only one number left, this is the value we want
## If none match in that column, move to the next column
