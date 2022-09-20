import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

N = int(input())
tree = [[] for _ in range(N+1)]
visitied = [0]*(N+1)

for i in range(N-1):
    p, c = map(int, input().rstrip().split())
    tree[p].append(c)
    tree[c].append(p)

def DFS(start, visitied, tree):
    for i in tree[start] :
        if not visitied[i] :
            visitied[i] = start
            DFS(i, visitied, tree)

DFS(1, visitied, tree)

for i in range(2, N+1) :
    print(visitied[i])