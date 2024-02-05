#input
n = int(input())
arr = [
    tuple(map(int, input().split()))
    for _ in range(n)
]

arrOneDimen = []
for i in range(n):
    for j in range(n):
        if not arr[i][j] in arrOneDimen:
            arrOneDimen.append(arr[i][j])
arrOneDimen.sort()

dp = [[-1 for _ in range(n)]for _ in range(n)]

dxs = [-1, 0, 1, 0]
dys = [0, -1, 0, 1]

def inRange(x,y):
    return x >= 0 and x < n and y >= 0 and y < n

#dp
for val in arrOneDimen:
    for i in range(n):
        for j in range(n):
            if arr[i][j] == val:
                dps = []
                for dx, dy in zip(dxs, dys):
                    new_i, new_j = i+dx, j+dy
                    if inRange(new_i, new_j) and arr[new_i][new_j] < arr[i][j]:
                        tmp = dp[new_i][new_j] 
                        dps.append(tmp)
                #if we have smaller neighbor 
                if len(dps) > 0:
                    dp[i][j] = max(dps)+1
                #otherwise
                else: dp[i][j] = 1
                
print(max(max(dp)))