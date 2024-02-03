n = int(input())

dp = [-1 for _ in range(n+1)]
dp[0] = 1
dp[1] = 2

def func(n):

    #fill up dp up to k
    for k in range(2, n+1):
        tmp = 0
        #get tmp val
        for l in range(0, k-2):
            tmp += (dp[l])*2 

        dp[k] = 2*dp[k-1] + 3*dp[k-2] + tmp

    return dp[n]
print(func(n))
# print(dp)