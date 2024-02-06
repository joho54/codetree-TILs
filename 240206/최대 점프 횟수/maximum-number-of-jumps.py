import sys
MIN_INT = -sys.maxsize
#input

n = int(input())

a = tuple(map(int, input().split()))
dp = [0 for _ in range(n)]
def initailize():
    for i in range(n):
        dp[i] = MIN_INT
    dp[0] = 0

initailize()

for i in range(1, n):
    for j in range(0, i):
        if dp[j] == MIN_INT:
            continue
        if a[j]+j >= i:
            dp[i] = max(dp[i], dp[j]+1)
ans = 0
for i in range(n):
    ans = max(ans, dp[i])
print(ans)