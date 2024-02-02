n = int(input())
memo = [-1 for _ in range(n+1)]

def fibo(n):
    if memo[n] != -1:
        return memo[n]
    if n == 1:
        memo[n] = 1
    elif n == 0:
        memo[n] = 0
    else: memo[n] = fibo(n-2)+fibo(n-1)
    return memo[n]

print(fibo(n))