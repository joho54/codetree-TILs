#input
n = int(input())
arr = [
    tuple(map(int, input().split()))
    for _ in range(n)
]

d = {}

for x, y in arr:
    if x in d:
        #update
        if d[x] > y:
            d[x] = y

    else: d[x] = y
ans = 0
for i in d:
    ans += d[i]
print(ans)