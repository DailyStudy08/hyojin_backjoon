from collections import deque
import queue


M, N, K = map(int, input().split())
arr = [[0]*N for _ in range(M)]

for i in range(K):
    x1, y1, x2, y2 = map(int, input().split())

    for i in range(y1, y2):
        for j in range(x1, x2) :
            arr[i][j] = 1

def bfs(i, j):
    queue = deque()
    queue.append((i,j))
    d = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    cnt = 1

    while queue:
        y, x = queue.popleft()

        for dy, dx in d:
            dy = y+dy
            dx = x+dx
            if 0<=dy<M and 0<=dx<N and not arr[dy][dx] :
                arr[dy][dx] = 1
                queue.append((dy, dx))
                cnt += 1
    
    return cnt

res = []
for i in range(M):
    for j in range(N):
        if not arr[i][j]:
            arr[i][j] = 1
            res.append(bfs(i,j))

print(len(res))
print(*sorted(res))