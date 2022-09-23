from collections import deque

def BFS(r, c):
    cnt = 0
    queue = deque()
    queue.append((r, c, cnt))

    while queue:
        current_r, current_c, cnt = queue.popleft()

        if current_r == end_x and current_c == end_y :
            print(cnt)
            return

        for i in d:
            nr = current_r+i[0]
            nc = current_c+i[1]

            if 0<=nr<I and 0<=nc<I and not chess[nr][nc]:
                chess[nr][nc] = 1
                queue.append((nr, nc, cnt+1))

T = int(input())

for tc in range(T):
    I = int(input())
    chess = [[0]*I for _ in range(I)]
    start_x, start_y = map(int, input().split())
    end_x, end_y = map(int, input().split())

    d = [(1,2),(2,1),(2,-1),(1, -2),(-1,-2),(-2,-1),(-2,1),(-1,2)]

    chess[start_x][start_y] = 1
    BFS(start_x, start_y)
