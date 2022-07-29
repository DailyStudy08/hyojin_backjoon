import sys

N = int(sys.stdin.readline())

num = list(map(int, sys.stdin.readline().split(' ')))

M = max(num)

avg = sum([(i/M)*100 for i in num])/N

print(avg)