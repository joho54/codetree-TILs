#input
n, m = tuple(map(int, input().split()))
arr = [
    input()
    for _ in range(n)
]
search = [
    input()
    for _ in range(m)
]

d1 = {}
d2 = {}

for i, e in enumerate(arr):
    d1[e] = i+1
    d2[i+1] = e


for s in search:
    if s in d1:
        print(d1[s])
    else:
        s = int(s)
        print(d2[s])