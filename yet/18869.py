import sys
input = sys.stdin.readline

M, N = map(int, input().split())
planets = {}

for i in range(M):
    lst = list(map(int, input().split()))
    k = sorted(list(set(lst)))
    dict_planet = {k[i]:i for i in range(N)}
    c = str([dict_planet[l] for l in lst])
    planets[c] = planets.get(c, 0)+1

print(sum(map(lambda x: x*(x-1)//2, planets.values())))
