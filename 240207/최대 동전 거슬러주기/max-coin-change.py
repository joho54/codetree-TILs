import sys
MIN_INT = -sys.maxsize

#input
n, m = tuple(map(int, input().split()))
coins = tuple(map(int, input().split()))

#initializing
#dp: 0~~m
dp = [MIN_INT for _ in range(m+1)]
dp[0] = 0


#fill dp
#i: dp index 1, 2, 3, 4, 5, 6, 7, 8
for i in range(1, m+1):
    #j: coin index 1, 2, 3
    for j in range(n):
        #impossible case
        if i >= coins[j]: 
            if dp[i-coins[j]] == MIN_INT:
                continue
            dp[i] = max(dp[i], dp[i-coins[j]]+1)

ans = -1
if dp[m] != MIN_INT:
    ans = dp[m]


print(ans)