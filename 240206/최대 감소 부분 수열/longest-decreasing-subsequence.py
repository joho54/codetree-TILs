#input

n = int(input())

a = tuple(map(int, input().split()))

dp = [0 for _ in range(n)]
dp[0] = 1

for i in range(1, n):
    tmp = [1]
    for j in range(i):
        if a[j] > a[i]:
            tmp.append(dp[j]+1)
    dp[i] = max(tmp)

print(max(dp))