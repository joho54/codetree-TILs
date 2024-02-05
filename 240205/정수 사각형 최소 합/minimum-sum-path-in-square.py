#input
n = int(input())
arr = [
    tuple(map(int, input().split()))
    for _ in range(n)
]

dp = [[0 for _ in range(n)] for _ in range(n)]
#start point: 0, n-1
dp[0][n-1] = arr[0][n-1]

#set dp

#vertical
for i in range(1, n):
    dp[i][n-1] = arr[i][n-1] + dp[i-1][n-1]

#horizontal
for j in range(n-2, -1, -1):
    dp[0][j] = arr[0][j] + dp[0][j+1]



for i in range(1, n):
    for j in range(n-2, -1, -1):
        dp[i][j] = min(dp[i][j+1]+arr[i][j], dp[i-1][j]+arr[i][j])
# for e in dp:
#     print(e)


print(dp[n-1][0])