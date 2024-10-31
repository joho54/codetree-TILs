# fractional knapsack problem

n, m = tuple(map(int, input().split()))
jewls = [
    tuple(map(int, input().split()))
    for _ in range(n)
]

jewls = sorted(jewls, key = lambda x: -x[1]/x[0]) 

weight_val = [(w, v/w) for w, v in jewls]
# print(weight_val)

ans = 0
cap = m # 남은 용량

for w, wv in weight_val:
    if cap - w >= 0:
        ans += w * wv
        cap -= w
    else:
        ans += cap * wv
        break

print("{:.3f}".format(ans))