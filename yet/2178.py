from collections import deque

N, M = map(int, input().split())
arr = [list(map(int, list(input()))) for _ in range(N)]
visited = [[0]*M for _ in range(N)]

def BFS(start):
    queue = deque()
    queue.append(start)

    while queue :
        r, c, cnt = queue.popleft()
        visited[r][c] = cnt
        
        for dr, dc in [(1,0),(-1,0),(0,1),(0,-1)]:
            nr, nc = r+dr, c+dc

            if 0<=nr<N and 0<=nc<M and not visited[nr][nc] and arr[nr][nc] :
                queue.append((nr, nc, cnt+1))

BFS((0,0,1))

print(visited[N-1][M-1])