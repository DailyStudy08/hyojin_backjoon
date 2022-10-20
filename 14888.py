import math
from itertools import permutations

N = int(input())
arr = list(map(int, input().split()))
operation = dict(pair for pair in zip(['+', '-', '*', '/'], list(map(int, input().split()))))
use = []

for i in operation.keys() :
    use.extend([i]*operation[i])

min_value, max_value = 1000000000, 0
for i in permutations(use, N-1):
    sum = arr[0]
    for j in range(1, N):
        if i[j-1] == '+':
            sum = sum+arr[j]
        elif i[j-1] == '-':
            sum = sum-arr[j]
        elif i[j-1] == '*':
            sum = sum*arr[j]
        else :
            sum = math.trunc(sum/arr[j])

    if sum < min_value :
        min_value = sum
    if sum > max_value :
        max_value = sum

print(max_value)
print(min_value)