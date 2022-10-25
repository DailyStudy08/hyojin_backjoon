INF = int(1e9)
N, E = map(int, input().split(' '))

graph = [[INF]*(N+1) for _ in range(N+1)]

for _ in range(E) :
    a, b, c = map(int, input().split(' '))
    graph[a][b] = c

start, end = map(int, input().split(' '))

def dijkstra(start) :
    distance = graph[start][:]

    visited = [0]*(N+1)
    visited[start] += 1
    distance[start] = 0

    while sum(visited) < N*2 :
        min_idx = 0
        min_val = INF

        for i in range(N+1) :
            if visited[i] < 2 and distance[i] < min_val :
                min_idx = i
                min_val = distance[i]
        
        visited[min_idx] += 1

        for i in range(N+1) :
            if visited[i] < 2 and distance[i] > min_val+graph[min_idx][i] :
                distance[i] = min_val+graph[min_idx][i]

        return distance

one = dijkstra(1)
two = dijkstra(start)
three = dijkstra(end)

cnt = min(one[start]+two[end]+three[N], one[end]+three[start]+two[N])

print(cnt if cnt<INF else -1)