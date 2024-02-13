n, k = tuple(map(int, input().split()))

arr = tuple(map(int, input().split()))

d = {}

for e in arr:
    if e in d:
        d[e] += 1
    else:
        d[e] = 1
        

d = sorted(d.items(), key=lambda x: x[1], reverse = True)
d = sorted(d, key= lambda x: (x[1], x[0]), reverse = True)

for i in range(k):
    print(d[i][0], end = ' ')