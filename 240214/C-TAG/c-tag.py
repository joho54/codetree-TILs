n, m = tuple(map(int, input().split()))
A = [
    input()
    for _ in range(n)
]
B = [
    input()
    for _ in range(n)
]

def inspectPattern(i, j, k):
    set1, set2 = set(), set()
    for line in A:
        set1.add((line[i], line[j], line[k]))
    for line in B:
        set2.add((line[i], line[j], line[k]))
    #now we have every pattern from A
    for s in set1:
        if s in set2:
            return False
    return True
    
ans = 0
#every pattern i, j, k
for i in range(m):
    for j in range(i+1, m):
        for k in range(j+1, m):
            if inspectPattern(i,j,k):
                ans += 1
print(ans)