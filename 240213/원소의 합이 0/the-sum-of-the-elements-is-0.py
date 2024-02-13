#input
n = int(input())
A = tuple(map(int, input().split()))
B = tuple(map(int, input().split()))
C = tuple(map(int, input().split()))
D = tuple(map(int, input().split()))

d = {}

#1. 모든 l 구해서 dictionary 만들기. l = C,D로 만들 수 있는 조합
for i in range(n):
    for j in range(n):
        l = C[i] + D[j]
        if l in d:
            d[l] += 1
        else: d[l] = 1
ans = 0
for i in range(n):
    for j in range(n):
        k = A[i]+B[j]
        if -k in d:
            ans += d[-k]
        
print(ans)