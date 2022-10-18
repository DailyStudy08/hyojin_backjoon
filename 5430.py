import sys
from collections import deque

T = int(input())

for _ in range(T):
    p = sys.stdin.readline().rstrip()
    n = int(input())
    lst = deque(sys.stdin.readline().rstrip()[1:-1].split(','))

    if not n : lst = deque()

    flag = 0
    for i in p:
        if i == 'R':
            lst.reverse()
        if i == 'D':
            if lst :
                lst.popleft()
            else :
                print('error')
                flag = 0
                break
    
    if flag :
        print('['+",".join(lst)+']')