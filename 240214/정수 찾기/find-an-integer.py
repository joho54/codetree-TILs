n1 = int(input())
arr1 = tuple(map(int, input().split()))
n2 = int(input())
arr2 = tuple(map(int, input().split()))

set1 = set(arr1)


for e in arr2:
    if e in set1:
        print(1)
    else:
        print(0)