# 배수가 아닌 동전 채우기. dp?

import sys

MAX_INT = sys.maxsize

n = int(input())
ans = 0

dp = [MAX_INT for _ in range(n+1)]

# dp[n] = n을 만들기 위해 필요한 최소 동전의 수
# dp[n] = min(dp[n-2], dp[n-5])+1

dp[2] = 1
dp[5] = 1

for i in range(6, n+1):
    dp[i] = min(dp[i-2], dp[i-5]) + 1

print(dp[n])