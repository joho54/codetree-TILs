#input
n = int(input())
arr = [
    tuple(map(int, input().split()))
    for _ in range(n)
]

#m: end of the date. iterated by i
m = 0
for i in range(n):
    if m < arr[i][1]:
        m = arr[i][1]

#dp
dp = [0 for _ in range(m+2)]

#set dp from backward
for i in range(m, -1, -1):
    dp[i] = dp[i+1]
    for k in range(n):
        if arr[k][0] == i:
            # print(k)
            dp[i] = max(dp[i], arr[k][2]) #만약 j가 없을 경우.
            for j in range(arr[k][1]+1, m+1): #
                # print('j', j)
                dp[i] = max(dp[i], dp[j]+arr[k][2])
print(dp[0])