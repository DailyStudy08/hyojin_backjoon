N = int(input())
area = []

for _ in range(N):
    area.append(list(input()))

visited = [[0]*(N) for _ in range(N)]

def DFS(start):
    if start == (N-1, N-1) :
        return
    
    

print(visited)