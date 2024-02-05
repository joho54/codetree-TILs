#input
n = int(input())
arr = [
    tuple(map(int, input().split()))
    for _ in range(n)
]

arrDetailed = []

for i in range(n):
    for j in range(n):
        arrDetailed.append((arr[i][j], i, j))

#(val, i, j)

arrDetailed.sort()


dp = [[1 for _ in range(n)]for _ in range(n)]
ans = 0
dxs = [-1, 0, 1, 0]
dys = [0, -1, 0, 1]

def inRange(x,y):
    return x >= 0 and x < n and y >= 0 and y < n

#dp
for details in arrDetailed:
    v, i, j = details
    for dx, dy in zip(dxs, dys):
        new_i, new_j = i+dx, j+dy
        if inRange(new_i, new_j) and arr[new_i][new_j] > arr[i][j]:
            dp[new_i][new_j] = max(dp[new_i][new_j], dp[i][j]+1)
            
    #if we have smaller neighbor 
# for i in range(n):
#     for j in range(n):
#         ans = max(ans, dp[i][j])

print(max(max(dp)))