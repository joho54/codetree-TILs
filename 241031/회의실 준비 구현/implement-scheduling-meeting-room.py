n = int(input())
arr = [
    tuple(map(int, input().split()))
    for _ in range(n)
]

arr = sorted(arr, key = lambda x: x[1])

ans = 1 # total count
last_elem = arr[0]

for elem in arr[1:]:
    if elem[0] >= last_elem[1]:
        last_elem = elem
        ans += 1
    

print(ans)