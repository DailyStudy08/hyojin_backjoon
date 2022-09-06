V = int(input())
E = int(input())

computers = [[] for _ in range(V+1)]
visited = [False]*(V+1)

for _ in range(E) :
    num1, num2 = map(int, input().split())

    computers[num1].append(num2)
    computers[num2].append(num1)

def DFS(i):
    visited[i] = True
    for j in computers[i]:
        if not visited[j]:
            DFS(j)

DFS(1)
print(visited.count(True)-1)