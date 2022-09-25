N = int(input())
map = [list(map(int, list(input()))) for _ in range(N)]
visited = [[0]*N for _ in range(N)]

def DFS(start, cnt) :
    stack = []
    stack.append(start)

    visited[start[0]][start[1]] = cnt
    while stack :
        r, c = stack.pop()

        for dr, dc in [(1,0), (-1,0), (0,1), (0,-1)]:
            nr, nc = r+dr, c+dc
            
            if 0<=nr<N and 0<=nc<N and not visited[nr][nc] and map[nr][nc]:
                visited[nr][nc] = cnt
                DFS((nr, nc),cnt)

cnt = 1
for i in range(N) :
     for j in range(N) :
        if not visited[i][j] and map[i][j] :
            DFS((i, j), cnt)
            cnt += 1

res = [0]*cnt
for i in range(N):
    for j in range(N):
        res[visited[i][j]] += 1

res = sorted(res[1:])

print(cnt-1)
for i in res:
    print(i)