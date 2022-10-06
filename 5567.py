n = int(input())
m = int(input())
friends = [[]*(n+1) for _ in range(n+1)]
visited = [False]*(n+1)
visited[1] = True

for _ in range(m) :
    a, b = map(int, input().split())

    friends[a].append(b)
    friends[b].append(a)

def DFS(start, depth):
    if depth == 2 :
        return

    for i in friends[start]:
        if not visited[i] :
            visited[i] = True
        DFS(i, depth+1)

DFS(1, 0)
print(visited[2:].count(True))