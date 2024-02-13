#input
n = int(input())

arr = [
    input()
    for _ in range(n)
]
#save all letter numbers into dictionary

dicArr = []
count = {}

for e in arr:
    d = {}
    for ee in e:
        if ee in d:
            d[ee] += 1
        else:
            d[ee] = 1
    new_arr = [
        [value, key]
        for key, value in d.items()
    ]

    new_arr = sorted(new_arr, key = lambda x: x[1])
    if new_arr in dicArr:
        count[str(new_arr)] += 1
    else:
        count[str(new_arr)] = 1
        dicArr.append(new_arr)

d2 = sorted(count.items(), key=lambda x: x[1], reverse=True)
print(d2[0][1])