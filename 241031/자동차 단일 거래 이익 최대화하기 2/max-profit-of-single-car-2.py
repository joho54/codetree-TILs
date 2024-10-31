# n = int(input())
# arr = tuple(map(int, input().split()))

# pre_sub = []

# for i in range(1, n):
#     pre_sub.append(arr[i] - arr[i-1])

# # print(pre_sub)

# ans = pre_sub[0]
# fin = pre_sub[0]

# for elem in pre_sub[1:]:
#     if ans < 0:
#         ans = elem
#     else:
#         ans += elem
#     fin = max(ans, fin)
#     # print(ans)

# fin = fin if fin > 0 else 0

# print(fin)

# inplace한 방식으로 바꿔 풀어봐라.

n = int(input())
arr = tuple(map(int, input().split()))

max_profit = 0
min_price = arr[0]

for i in range(1, n):
    # updpate profit
    profit = arr[i] - min_price

    if profit > max_profit:
        max_profit = profit
    
    # update min price
    if arr[i] < min_price:
        min_price = arr[i]

profit = profit if profit > 0 else 0

print(profit)