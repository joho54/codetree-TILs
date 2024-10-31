# 배수일 떄는 그냥 큰동전부터 담는게 이득인 그리디 문제

# 입력
n, k = tuple(map(int, input().split()))
coins = [0 for _ in range(n)]
for i in range(n):  
    coins[i] = int(input())

cnt = 0 # increment. 

for coin in coins[-1::-1]:  # 각각 큰 동전에 대해 루프를 거꾸로
    # this is not good
    # while k - coin >= 0:
    #     k -= coin
    #     cnt += 1 
    cnt = cnt + k // coin
    k = k % coin

print(cnt)