#inpu
n, m = tuple(map(int, input().split()))
arr = tuple(map(int, input().split()))
indices = tuple(map(int, input().split()))

d = {}

for idx in indices:
    ans = 0
    for i, enum in enumerate(arr):
        if idx == enum:
            ans += 1
    print(ans, end = ' ')