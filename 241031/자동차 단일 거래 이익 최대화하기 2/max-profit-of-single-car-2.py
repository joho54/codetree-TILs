# 변수 선언 및 입력:
n = int(input())
price = list(map(int, input().split()))

# 배열을 앞에서부터 순회하며 최소값을 갱신해줍니다.
# 각 원소에 대하여 해당 시점의 최소값과의 차이가
# 최대가 될 때를 갱신해줍니다.
max_profit = 0
min_price = price[0]
for i in range(n):
    profit = price[i] - min_price

    # 답을 갱신해줍니다.
    if profit > max_profit:
        max_profit = profit

    # 지금까지의 최솟값을 갱신해줍니다.
    if min_price > price[i]:
        min_price = price[i]
    
print(max_profit)