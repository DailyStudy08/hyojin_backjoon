N = int(input())
M = int(input())

city = [[0xffffff]*(N+1) for _ in range(N+1)]

for _ in range(M):
    start, end, price = map(int, input().split())
    city[start][end] = price

A, B = map(int, input().split())

def dijkstra(s) :
    distance = city[s][:]
    visitied = [0]*(N+1)
    visitied[s] = 1
    distance[s] = 0

    while sum(visitied) <= N :
        min_idx, min_val = 0, 0xffffff

        for i in range(N+1) :
            if not visitied[i] and distance[i] < min_val :
                min_idx = i
                min_val = distance[i]

        visitied[min_idx] = 1

        for i in range(N+1) :
            if not visitied[i] and distance[i] > min_val+city[min_idx][i]:
                distance[i] = min_val+city[min_idx][i]
    return distance

print(dijkstra(A)[B])