import sys

N = int(sys.stdin.readline())

all = []

for i in range(0,N) :
    x,y = map(int, sys.stdin.readline().split(' '))
    all.append((x,y))
    
res = [1 for i in range(0,N)]

for n in range(0,N) :
    for m in range(0, N) :
        if n == m : continue
        else :
            if all[n][0]>all[m][0] and all[n][1]>all[m][1] :
                res[m] += 1
            else : continue

print(" ".join(map(str,res)))