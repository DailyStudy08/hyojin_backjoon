from itertools import combinations

N, M = map(int, input().split(" "))
cards = list(map(int, input().split(" ")))
sum = [sum(i) for i in list(combinations(cards, 3))]
res = 0

for i in sum :
    if i <= M and i>res :
        res = i

print(res)