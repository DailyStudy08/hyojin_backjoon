from collections import deque

M, N = map(int, input().split())
box, tomato = [], deque()

for i in range(N) :
    tmp = list(map(int, input().split()))
    for j in range(M) :
        if tmp[j] == 1 :
            tomato.append((i, j))
    box.append(tmp)

clear = [[1]*M for _ in range(N)]

def BFS() :
    while tomato :
        r, c = tomato.popleft()

        for dr, dc in [(0, 1), (0,-1), (1,0), (-1,0)]:
            nr, nc = r+dr, c+dc

            if 0<=nr<N and 0<=nc<M and not box[nr][nc]:
                box[nr][nc] = box[r][c]+1
                tomato.append((nr, nc))

BFS()

res = 0
for i in box :
    for j in i :
        if not j :
            print(-1)
            exit(0)
    res = max(res, max(i))

print(res-1)