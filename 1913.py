N = int(input())
num = int(input())

res = [[0]*N for _ in range(N)]

# bottom right top left
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
x, y, n_direct = 0, 0, 0

for i in range(N*N, 0, -1):
    res[x][y] = i

    x += dx[n_direct]
    y += dy[n_direct]

    if x == N or y == N or x<0 or y<0 or res[x][y] :
        x -= dx[n_direct]
        y -= dy[n_direct]

        n_direct = (n_direct+1)%4

        x += dx[n_direct]
        y += dy[n_direct]

for j in range(N):
    print(*res[j])
    if num in res[j]:
        mx = j + 1
        my = res[j].index(num) + 1
print(mx, my)