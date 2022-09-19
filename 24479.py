from re import L


N, M, R = map(int, input().split())

graph = [[] for _ in range(N+1)]

for i in range(M):
    u, v = map(int, input().split())

    graph[u].append(v)
    graph[v].append(u)

for i in graph :
    i.sort(reverse=True)

def dfs(R) :
    stack = [R]
    visited = [False]*(N+1)
    res = [0]*(N+1)
    cnt = 1

    while stack:
        value = stack.pop()
        
        if visited[value] :
            continue

        visited[value] = 1
        res[value] = cnt
        cnt+=1

        for i in graph[value]:
            if not visited[i]:
                stack.append(i)

    return res

for i in dfs(R)[1:] :
    print(i)