import sys
from itertools import combinations

L, C = map(int, sys.stdin.readline().split())
arr = sorted(sys.stdin.readline().split())
vowel = {'a', 'e', 'i', 'o', 'u'}
consonant = set(arr)-(set(vowel)&set(arr))

def make_code():
    res = []
    for i in combinations(arr, L):
        if len(set(i)&vowel) >0 and len(set(i)&consonant) > 1 :
            res.append(''.join(i))

    return res

for p in make_code():
    print(p)