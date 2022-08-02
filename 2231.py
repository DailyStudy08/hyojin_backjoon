import sys

N = int(sys.stdin.readline())

for i in range(1, N) :
    target = sum(map(int, str(i)))
    if target+i == N :
        print(i)
        break
else:
    print(0)