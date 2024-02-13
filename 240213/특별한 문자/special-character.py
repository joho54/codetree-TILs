arr = input()

d = {}

for e in arr:
    if e in d:
        d[e] += 1
    else: d[e] = 1

# print(d)
ls = sorted(d.items(), key = lambda x: x[1])
# print(ls)
if ls[0][1] == 1:
    print(ls[0][0])
else:
    print('None')