import sys
N = int(sys.stdin.readline())

words = []
for i in range(0,N) :
    words.append(sys.stdin.readline().strip())

words = sorted(sorted(list(set(words))), key=len)

for i in words :
    print(i)