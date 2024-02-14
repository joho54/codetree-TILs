ans = 0

n = int(input())
arr = tuple(map(int, input().split()))

set1 = set()

for e in arr:
    if e not in set1:
        ans += 1
        set1.add(e)

print(ans)