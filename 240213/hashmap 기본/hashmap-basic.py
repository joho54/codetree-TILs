n = int(input())
orders = [
    tuple(map(str, input().split()))
    for _ in range(n)
]
d = dict()

for o in orders:
    if o[0] == 'add':
        d[o[1]] = o[2]
    elif o[0] == 'find':
        if o[1] in d:
            print(d[o[1]])
        else:
            print('None')
    elif o[0] == 'remove':
        d.pop(o[1])