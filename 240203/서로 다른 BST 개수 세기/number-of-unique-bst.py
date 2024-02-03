n = int(input())

dp = [-1 for _ in range(n+1)]
#get n
dp[0] =1
dp[1] =1
if n >= 2:
    dp[2] = 2
#idx: dp index
for idx in range(2,n+1): #2,3
    #sigma
    tmp = 0
    for rootIdx in range(0, idx):
        tmp += dp[rootIdx]*dp[idx-1-rootIdx]
    dp[idx] = tmp
    
print(dp[n])