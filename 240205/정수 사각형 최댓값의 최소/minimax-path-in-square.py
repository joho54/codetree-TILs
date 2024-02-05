#input
n = int(input())
arr = [
    tuple(map(int, input().split()))
    for _ in range(n)
]

dp = [[0 for _ in range(n)] for _ in range(n)]
#start point: 0, 0
dp[0][0] = arr[0][0]

#set dp

#vertical
for i in range(1, n):
    dp[i][0] = max(arr[i][0], dp[i-1][0])

#horizontal
for j in range(1, n):
    dp[0][j] = max(arr[0][j], dp[0][j-1])



for i in range(1, n):
    for j in range(1, n):
        dp[i][j] = min(max(arr[i][j], dp[i-1][j]), max(arr[i][j], dp[i][j-1]))
# for e in dp:
#     print(e)


print(dp[n-1][n-1])