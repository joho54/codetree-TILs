from sortedcontainers import SortedDict

sd = SortedDict() 

n = int(input())
orders = [
    list(map(str, input().split()))
    for _ in range(n)
]

for o in orders:
    for i in range(1, len(o)):
        o[i] = int(o[i])
    if o[0] == 'add':
        sd[o[1]] = o[2]
    elif o[0] == 'remove':
        sd.pop(o[1])
    elif o[0] == 'find':
        if o[1] in sd:
            tmp = sd[o[1]]
            print(tmp)
        else:
            print("None")
    elif o[0] == 'print_list':
        if sd:  
            for _, val in sd.items():
                print(val, end = ' ')
            print()
        else:
            print("None")