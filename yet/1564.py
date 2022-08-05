import sys

def factorial(N) :
    return factorial(N-1)*N if N>1 else 1

N = str(factorial(int(sys.stdin.readline())))
cnt = 0
res = []

for i in range(len(N)-1,0,-1) :
    if N[i]=='0' and cnt == 0 :
        continue
    else :
        res.insert(0, N[i])
        cnt +=1

print(''.join(res)[-5:])