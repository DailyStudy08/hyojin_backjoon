import math
import sys

T = int(sys.stdin.readline())
hotel = []

for j in range (T):
    tmp = map(int,sys.stdin.readline().split(' '))
    hotel.append(list(tmp))

for k in hotel :
    # num = str(abs(k[2]-k[0]))+str(abs(k[1]-k[0])) if k[1]//k[0]<10
    # print(num)
    pass


print(hotel)