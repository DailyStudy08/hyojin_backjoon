T = int(input())

def DFS(start, cnt) :
    stack = []
    stack.append(start)

    while stack:
        r, c = stack.pop()

        if visited[r][c] :
            continue

        visited[r][c] = cnt
        for dr, dc in [(0,1), (1,0),(0,-1),(-1,0)]:
            nr, nc = r+dr, c+dc

            if 0<=nr<N and 0<=nc<M and not visited[nr][nc] and field[nr][nc] :
                stack.append((nr, nc))

for tc in range(T):
    M, N, K = map(int, input().split())

    field = [[0]*(M) for _ in range(N)]

    cabbage = []
    for i in range(K) :
        x, y = map(int, input().split())
        field[y][x] = 1
        cabbage.append((y, x))

    visited = [[0]*(M) for _ in range(N)]

    for i in range(len(cabbage)):
        DFS(cabbage[i], i+1)

    cnt = set()
    for i in range(N):
        for j in range(M):
            tmp = visited[i][j]
            if tmp :
                cnt.add(tmp)

    print(len(cnt))