N = int(input())

lst = [list(map(int, input().split())) for _ in range(N)]

for i in range(N) :
    for j in range(N) :
        if lst[i][0] < lst[j][0] :
            lst[i], lst[j] = lst[j], lst[i]

for i in range(N-1) :
    if lst[i][0] == lst[i+1][0] and lst[i][1] > lst [i+1][1] :
        lst[i], lst[i+1] = lst[i+1], lst[i]

for i in range(N) :
    print(f'{lst[i][0]} {lst[i][1]}')