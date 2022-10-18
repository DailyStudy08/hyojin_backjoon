def DFS(start, high, cnt) : 
    stack = []
    stack.append(start)

    while stack :
        r, c = stack.pop()
        visited[r][c] = cnt
        
        for dr, dc in [(0,1), (1,0), (0, -1), (-1,0)] :
            nr, nc = r+dr, c+dc

            if 0<=nr<N and 0<=nc<N and not visited[nr][nc] and area[nr][nc]>high :
                stack.append((nr, nc))
                visited[nr][nc] = cnt

N = int(input())
area = [list(map(int, input().split())) for _ in range(N)]
min_value, max_value = 100, 0

idx_lst = []

for k in range(min(min(area)), max(max(area))) :
    visited = [[0]*N for _ in range(N)]
    will_visited = []
    high = k

    idx = 0
    for i in range(0, N):
        for j in range(0, N) :
            if area[i][j] > high and not visited[i][j] :
                idx += 1
                DFS((i, j), high, idx)
    idx_lst.append(idx)

print(max(idx_lst) if idx_lst else 1)