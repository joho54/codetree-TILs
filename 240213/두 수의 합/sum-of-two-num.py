#input
n, k = tuple(map(int ,input().split()))
arr = tuple(map(int ,input().split()))

#해쉬 맵으로 [k-현재 고른 숫자]를 찾으면 됨. 이 키가 있는지

d = {}

for i, e in enumerate(arr):
    d[e] = i
ans = 0 
for i, e in enumerate(arr):
    if (k-e) in d:
        ans += 1
print(ans//2)