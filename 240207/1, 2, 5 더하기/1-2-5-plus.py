#dp: n, i
#A: m, j

#input
n = int(input())
m = 3
#dp
dp = [0 for _ in range(n+1)]
dp[0] = 1
#A
A = [1, 2, 5]

#dp
for i in range(1, n+1):
    for j in range(m):
        if i >= A[j]:
            if dp[i-A[j]] == 0:
                continue
            dp[i] = dp[i] + dp[i-A[j]]

print(dp[n]%10007)