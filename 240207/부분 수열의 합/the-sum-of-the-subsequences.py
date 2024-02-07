#A: i, n
#dp: j,m 

#input
n, m = tuple(map(int, input().split()))
A = tuple(map(int, input().split()))

#dp: m
dp = [False for _ in range(m+1)]

dp[0] = True

for i in range(n):
    for j in range(m, 0, -1):
        if j >= A[i]:
            if not dp[j-A[i]]:
                continue
            dp[j] = dp[j-A[i]]

if dp[m]:
    print('Yes')
else:
    print('No')