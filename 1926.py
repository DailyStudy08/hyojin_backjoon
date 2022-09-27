n, m = map(int, input().split())
art = [list(map(int, input().split())) for _ in range(n)]
visited = [[0]*m for _ in range(n)]

def DFS(start, cnt) :
    stack = []
    stack.append(start)
    visited[start[0]][start[1]] = cnt

    while stack:
        r, c = stack.pop()

        for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            nr, nc = r+dr, c+dc

            if 0<=nr<n and 0<=nc<m and not visited[nr][nc] and art[nr][nc]:
                visited[nr][nc] = cnt
                stack.append((nr, nc))

cnt = 1
for i in range(n):
    for j in range(m):
        if art[i][j] and not visited[i][j]:
            DFS((i, j), cnt)
            cnt += 1

res = [0]*cnt
for i in range(n):
    for j in range(m):
        res[visited[i][j]] += 1

print(len(res[1:]))

try :
    print(max(res[1:]))
except :
    print(0)