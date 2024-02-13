#inpu
n, m = tuple(map(int, input().split()))
arr = tuple(map(int, input().split()))
indices = tuple(map(int, input().split()))

d = {}


for enum in arr:
    if enum in d:
        d[enum] += 1
    else:
        d[enum] = 1

for idx in indices:
    if idx in d:
        print(d[idx], end = ' ')
    else:
        print(0, end = ' ')