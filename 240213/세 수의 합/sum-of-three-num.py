#input
n, k = tuple(map(int, input().split()))
arr = tuple(map(int, input().split()))

d = {}

# d[arr[0]] = 1
ans =0
for i, e in enumerate(arr):
    diff1 = k-e
    for j in range(i+1, n):
        diff2 = diff1 - arr[j]
        if diff2 in d:
            ans += d[diff2]
        
    if e in d:
        d[e] += 1
    else:
        d[e] = 1
print(ans)