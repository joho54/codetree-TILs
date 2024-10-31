# # 배수가 아닌 동전 채우기. dp?

# import sys

# MAX_INT = sys.maxsize

# n = int(input())
# ans = 0

# dp = [MAX_INT for _ in range(n+1)]

# # dp[n] = n을 만들기 위해 필요한 최소 동전의 수
# # dp[n] = min(dp[n-2], dp[n-5])+1

# def initialize(n):
#     init_arr = [0 , MAX_INT, 1, MAX_INT, 2, 1] # 5
#     n = n if n < 6 else 6
#     for i in range(0, n): # 
#         dp[i] = init_arr[i]

# initialize(n)

# for i in range(6, n+1):
#     dp[i] = min(dp[i-2], dp[i-5]) + 1

# ans = dp[n] if dp[n] != MAX_INT else -1
# print(ans)

# greedy하게 풀면 5원 먼저 최대한 집어넣는거임

# 다시 풀어보자


MAX_INT = 100000

n = int(input())
ans = MAX_INT # 왜 max_int로 초기화해도 괜찮은 거지? tmp는 이것보단 무조건 작을 테니까?

for i in range(n+1): #왜 max_int + 1 인거지? i가 그만큼 커질 필요가 있나?
    k = n - 5 * i 
    if k >= 0:
        if k%2 == 0:
            tmp = i + k//2
            ans = min(tmp, ans)

ans = ans if ans != MAX_INT else -1
print(ans)