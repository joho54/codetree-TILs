_, _ = tuple(map(int, input().split()))
A = tuple(map(int, input().split()))
B = tuple(map(int, input().split()))

aSet = set(A)
bSet = set(B)
ans = 0
for e in A:
    if e not in bSet:
        ans += 1
for e in B:
    if e not in aSet:
        ans += 1
print(ans)