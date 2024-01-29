#grid, dfs(4 directions)
#for against dfs

n = int(input())

grid = [
    tuple(map(int, input().split()))
    for _ in range(n)
]

villages = [0]
villIdx = 0

visited = [[False for _ in range(n)] for _ in range(n)]

def inRange(x, y):
    return x >= 0 and x < n and y >= 0 and y < n

def canGo(x, y):
    #in range, no wall, not visited
    if inRange(x, y) and grid[x][y] != 0 and not visited[x][y]:
        return True
    return False

def dfs(x, y):
    dxs = [0, -1, 0, 1]
    dys = [1, 0, -1, 0]

    for dx, dy in zip(dxs, dys):
        new_x, new_y = x+dx, y+dy
        if canGo(new_x, new_y):
            #dfs
            villages[villIdx] += 1
            visited[new_x][new_y] = True
            dfs(new_x, new_y)

for i in range(n):
    for j in range(n):
        if canGo(i, j):
            visited[i][j] = True
            villages.append(1)
            villIdx += 1
            dfs(i, j)
villages.remove(villages[0])
villages.sort()
print(len(villages))
for l in villages:
    print(l)