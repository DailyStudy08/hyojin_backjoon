N, M = map(int, input().split())
city = [[0]*(N+1) for _ in range(N+1)]

for _ in range(M) :
    A, B, C = map(int, input().split())

    city[A][B] = C
    city[B][A] = C

mst = set()
mst_value = 0
weights = [0xffffff]*(N+1)
weights[1] = 0

while len(mst) <= N-1 :
    min_v = 0xffffff
    min_idx = 1

    for i in range(1, N+1) :
        if i not in mst and weights[i] < min_v:
            min_idx = i
            min_v = weights[i]

    mst.add(min_idx)
    mst_value += min_v

    for i in range(1, N+1) :
        if i not in mst and city[min_idx][i] and city[min_idx][i] < weights[i] :
            weights[i] = city[min_idx][i]

max_v = 0

for i in range(1, N+1) :
    if weights[i] > max_v:
        max_v = weights[i]

print(mst_value-max_v)