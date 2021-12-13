from collections import Counter
from aoctools import inputs
input = inputs(3,2021).get_input().splitlines

gamma_rate = epsilon_rate = ""
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
print(f'Answer (Power Consumption): {gamma_int*epsilon_int}')