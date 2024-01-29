#canGo = in range, heightSafe, not visited, 
import sys
sys.setrecursionlimit(1000000)

# 원래 코드 

#input
n, m = tuple(map(int, input().split()))
villages = [
    tuple(map(int, input().split()))
    for _ in range(n)
]

def inRange(x, y):
    return x >= 0 and x < n and y >= 0 and y < m

def isSafeHeight(x, y, k):
    return villages[x][y] > k

def canGo(x, y, k):
    if inRange(x, y) and isSafeHeight(x, y, k) and not visited[x][y]:
        return True
    return False

def dfs(x, y, k):
    dxs = [0, -1, 0, 1]
    dys = [1, 0, -1, 0]

    for dx, dy in zip(dxs, dys):
        new_x , new_y = x+dx, y+dy
        if canGo(new_x, new_y, k):
            #then?
            visited[new_x][new_y] = True
            dfs(new_x, new_y, k)


minK = 1
maxK = max(max(villages))

safeAreaOnK = [0 for _ in range(0, maxK+1)]

#dfs
for k in range(minK, maxK+1):#1~~~7
    visited = [[False for _ in range(m)] for _ in range(n)]
    for i in range(n):
        for j in range(m):
            if canGo(i, j, k):
                safeAreaOnK[k] += 1
                visited[i][j] = True
                dfs(i,j,k)
# print(safeAreaOnK)
maxVal, maxIdx = safeAreaOnK[1],1
for i in range(2, len(safeAreaOnK)):
    if maxVal < safeAreaOnK[i]:
        maxVal = safeAreaOnK[i]
        maxIdx = i
print(maxIdx, maxVal)