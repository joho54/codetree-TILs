#input
n = int(input())
lines = [
    tuple(map(int, input().split()))
    for _ in range(n)
]

dp = [1 for _ in range(n)]

dp[0] = 1

for i in range(1, n):
    for j in range(0, i):
        if lines[j][1] < lines[i][0]:
            dp[i] = max(dp[j]+1, dp[i])

print(dp[n-1])