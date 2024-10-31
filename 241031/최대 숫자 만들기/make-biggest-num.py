from functools import cmp_to_key

n = int(input())
arr = [
    int(input())
    for _ in range(n)
]

def compare(x, y):
    xy = int("{}{}".format(x, y))
    yx = int("{}{}".format(y, x))
    if xy > yx:
        return -1
    elif yx > xy:
        return 1
    else: return 0

arr.sort(key=cmp_to_key(compare))

for e in arr:
    print(e, end='')