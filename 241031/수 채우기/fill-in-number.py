# 배수가 아닌 동전 채우기. dp?

import sys

MAX_INT = sys.maxsize

n = int(input())
ans = 0

dp = [MAX_INT for _ in range(n+1)]

# dp[n] = n을 만들기 위해 필요한 최소 동전의 수
# dp[n] = min(dp[n-2], dp[n-5])+1



def initialize(n):
    init_arr = [0 , MAX_INT, 1, MAX_INT, 2, 1] # 5
    n = n if n < 6 else 6
    for i in range(0, n): # 
        dp[i] = init_arr[i]

initialize(n)

for i in range(6, n+1):
    dp[i] = min(dp[i-2], dp[i-5]) + 1

ans = dp[n] if dp[n] != MAX_INT else -1
print(ans)