#input
n = int(input())
arr = [
    tuple(map(str,input().split()))
    for _ in range(n)
]


d = {}
for e in arr:
    if e in d:
        d[e] += 1
    else:
        d[e] = 1
maxNum = 0

for e in d:
    if d[e] > maxNum:
        maxNum = d[e]
print(maxNum)