s = set()
n = int(input())
order = [
    tuple(map(str, input().split()))
    for _ in range(n)
]

for o in order:
    if o[0] == 'find':
        if int(o[1]) in s:
            print('true')
        else:
            print('false')

    elif o[0] == 'add':
        s.add(int(o[1]))
        # print(s)

    elif o[0] == 'remove':
        s.remove(int(o[1]))