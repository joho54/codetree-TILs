#input
n, k = tuple(map(int ,input().split()))
arr = tuple(map(int ,input().split()))

#해쉬 맵으로 [k-현재 고른 숫자]를 찾으면 됨. 이 키가 있는지

d = {}

#
for i, e in enumerate(arr):
    d[e] = i
ans = 0 
for i, e in enumerate(arr):
    #현재 주목한 배열보다 뒤에 있는 값들만 고려하려면?
    if (k-e) in d and i < d[k-e]:
        ans += 1
print(ans)