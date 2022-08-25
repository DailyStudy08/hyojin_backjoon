import sys
import heapq       # min heap

N = int(sys.stdin.readline())

heap = []

for i in range(N) :
    tmp = int(sys.stdin.readline())

    if tmp>0:
        heapq.heappush(heap,-tmp)
    elif tmp == 0:
        try:
            p = -heapq.heappop(heap)

            print(p)
        except:
            print(0)