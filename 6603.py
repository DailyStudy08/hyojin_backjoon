from itertools import combinations

while True :
    tc = list(map(int, input().split()))
    if not tc[0] : break
    k = tc[0]
    num_lst = tc[1:]
    res = set()

    for i in combinations(num_lst, 6):
        if i in res : continue
        else :
            res.add(i)

    for i in sorted(list(res)):
        print(' '.join(map(str, list(i))))
    print()