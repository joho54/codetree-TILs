#input
n = int(input())
arr = [
    tuple(map(int, input().split()))
    for _ in range(n)
]

dp = [[[0, 0, 0] for _ in range(n)] for _ in range(n)]
#start point: 0, 0
dp[0][0] = [0, arr[0][0], arr[0][0]]

#set dp

#vertical
for i in range(1, n):
    minValTmp = dp[i-1][0][1]
    maxValTmp = dp[i-1][0][2]
    if minValTmp > arr[i][0]:
        minValTmp = arr[i][0]
    if maxValTmp < arr[i][0]:
        maxValTmp = arr[i][0]
    ansVal = maxValTmp - minValTmp
    dp[i][0] = [ansVal, minValTmp, maxValTmp] 

#horizontal
for j in range(1, n):
    minValTmp = dp[0][j-1][1]
    maxValTmp = dp[0][j-1][2]
    if minValTmp > arr[0][j]:
        minValTmp = arr[0][j]
    if maxValTmp < arr[0][j]:
        maxValTmp = arr[0][j]
    ansVal = maxValTmp - minValTmp
    dp[0][j] = [ansVal, minValTmp, maxValTmp] 


def calc(ls, val):
    v, minVal, maxVal = ls
    #update min, max
    if minVal > val: minVal = val
    if maxVal < val: maxVal = val
    return (maxVal - minVal, minVal, maxVal)


for i in range(1, n):
    for j in range(1, n):
        val1, minVal1, maxVal1 = calc(dp[i-1][j], arr[i][j])
        val2, minVal2, maxVal2 = calc(dp[i][j-1], arr[i][j])
        
        if val1 < val2:
            dp[i][j] = [val1, minVal1, maxVal1]
        elif val1 > val2:
            dp[i][j] = [val2, minVal2, maxVal2]
        else:
            avgVal1 = (maxVal1 + minVal1)//2
            avgVal2 = (maxVal2 + minVal2)//2
            if abs(avgVal1-arr[i][j]) < abs(avgVal2-arr[i][j]):
                dp[i][j] = [val1, minVal1, maxVal1]
            else:
                dp[i][j] = [val2, minVal2, maxVal2]
            
# for e in dp:
#     print(e)


print(dp[n-1][n-1][0])