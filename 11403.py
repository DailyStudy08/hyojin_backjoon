N = int(input())
arr = [[0]*N for _ in range(N)]

for i in range(N):
    for j, k in enumerate(map(int,input().split())):
        arr[i][j] = k

for k in range(N):
    for i in range(N):
        for j in range(N):
            if arr[i][k] and arr[k][j]:
                arr[i][j] = 1

for i in arr :
    print(*i)