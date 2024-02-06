import sys
MIN_INT = -sys.maxsize

#input
n, m = tuple(map(int, input().split()))
arr = [
    tuple(map(int, input().split()))
    for _ in range(n)
]

dp = [
    [0 for _ in range(m)]
    for _ in range(n)
]

def initialize():
    for i in range(n):
        for j in range(m):
            dp[i][j] = MIN_INT
initialize()

# for i in range(n):
#     dp[i][0] = 0
    
# for j in range(m):
#     dp[0][j] = 0

dp[0][0] = 1

for i in range(1,n):
    for j in range(1,m):
        for k in range(0,i):
            for l in range(0, j):
                if dp[k][l] == MIN_INT:
                    continue
                if arr[i][j] > arr[k][l] and i >= k+1 and j >= l+1:
                    dp[i][j] = max(dp[i][j], dp[k][l]+1)

ans = 0
for i in range(n):
    for j in range(m):
        ans = max(dp[i][j], ans)
print(ans)

# for e in dp:
#     print(e)