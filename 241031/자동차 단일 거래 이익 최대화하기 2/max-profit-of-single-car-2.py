n = int(input())
arr = tuple(map(int, input().split()))

# prefix sub = 1 -8 1 3
# 이거 아까 그 뭐냐 그거, 최대합 만드는 문제랑 같음

pre_sub = []

for i in range(1, n):
    pre_sub.append(arr[i] - arr[i-1])

# print(pre_sub)

ans = pre_sub[0]
fin = pre_sub[0]

for elem in pre_sub[1:]:
    if ans < 0:
        ans = elem
    else:
        ans += elem
    fin = max(ans, fin)
    # print(ans)

fin = fin if fin > 0 else 0

print(fin)