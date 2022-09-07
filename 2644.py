N = int(input())
n1, n2 = map(int, input().split())
M = int(input())

family = [[] for _ in range(N+1)]
visited = [False]*(N+1)
res = []

for _ in range(M) :
    x, y = map(int, input().split())

    family[x].append(y)
    family[y].append(x)

def DFS(start, cnt):
    visited[start] = True
    
    if start == n2 :
        res.append(cnt)
    else :
        cnt += 1
    
        for i in family[start]:
            if not visited[i]:
                DFS(i, cnt)

DFS(n1, cnt=0)

print(res[0] if res else -1)