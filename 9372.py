T = int(input())

def DFS(start) :
    global cnt
    visitied[start] = True
    cnt += 1

    for i in nation[start] :
        if not visitied[i] :
            DFS(i)

for _ in range(T):
    N, M = map(int, input().split())

    nation = [[]*(N+1) for _ in range(N+1)]
    visitied = [False]*(N+1)
    for _ in range(M):
        a, b = map(int, input().split())

        nation[a].append(b)
        nation[b].append(a)

    cnt = 0
    DFS(1)
    print(cnt-1)