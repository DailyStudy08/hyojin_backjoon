import sys

#Bubble

N, K = list(map(int, sys.stdin.readline().split()))

arr = list(map(int, sys.stdin.readline().split()))

cnt = 0
ans = -1

for j in range(N-1, 0, -1) :
    for i in range(j) :
        if arr[i] > arr[i+1] :
            arr[i], arr[i+1] = arr[i+1], arr[i]
            cnt+=1
            if cnt == K :
                ans = f'{arr[i]} {arr[i+1]}'

print(ans)