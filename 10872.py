import sys

def factorial(N) :
    return factorial(N-1)*N if N>1 else 1

N = factorial(int(sys.stdin.readline()))

print(N)