N, M = map(int, input().split())
maze = [list(map(int, list(input()))) for _ in range(N)]
visited = [[0]*(M) for _ in range(N)]

print("maze")
for i in maze :
    print(i)

def DFS(r, c, dis):
    visited[r][c] = 1
    
    print("visited")
    for i in visited:
        print(i)
    
    print()

    if r == N-1 and c == M-1 : return dis

    min_dis = 1000000

    for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        nr, nc = r+dr, c+dc

        if 0<=nr<N and 0<=nc<M and maze[nr][nc] and not visited[nr][nc]:

            res = DFS(nr, nc, dis+1)

            if min_dis > res:
                min_dis = res

    return min_dis

print(DFS(0, 0, 1))