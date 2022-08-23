def fibo_recursive(n):
    if n<2: return n
    else : return fibo_recursive(n-1)+fibo_recursive(n-2)

def fibo_memoize(n):
    global memo
    if n >= 2 and len(memo) <= n :
        memo.append(fibo_memoize(n-1)+fibo_memoize(n-2))
    return memo[n]

def fibo_DP(n):
    f = [0,1]

    for i in range(2, n+1):
        f.append(f[i-1]+f[i-2])

    return f[n]

N=int(input())
memo = [0, 1]
print(fibo_DP(N))