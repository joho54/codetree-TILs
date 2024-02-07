import sys

MAX_INT = sys.maxsize

#j, m : dp index
#i, n: A index
#input
n, m = tuple(map(int, input().split()))

A = tuple(map(int, input().split()))

#dp: dp len = 0~~m
dp = [MAX_INT for _ in range(m+1)]
dp[0] = 0

#initialize dp
for i in range(0, n):  
    for j in range(m, -1, -1): 
        #same condition with finding max
        if j >= A[i]:
            if dp[j-A[i]] == MAX_INT:
                continue
            dp[j] = min(dp[j], dp[j-A[i]]+1)

ans = dp[m]
if ans == MAX_INT:
    ans = -1

print(ans)