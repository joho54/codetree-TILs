#cango in range, sameNum, visited


n = int(input())

grid = [
    tuple(map(int, input().split()))
    for _ in range(n)
]

visited = [[False for _ in range(n)] for _ in range(n)]

def inRange(x, y):
    return x >= 0 and x < n and y >= 0 and y < n

def sameNum(x, y, k):
    return grid[x][y] == k

def canGo(x, y, k):
    if inRange(x, y) and sameNum(x, y, k) and not visited[x][y]:
        return True
    return False

def dfs(x, y, k):
    dxs = [0, -1, 0, 1]
    dys = [1, 0, -1, 0]

    for dx, dy in zip(dxs, dys):
        new_x, new_y = x+dx, y+dy
        if canGo(new_x, new_y, k):
            visited[new_x][new_y] = True
            sizeOfBlocks[len(sizeOfBlocks)-1] += 1
            dfs(new_x,new_y, k)

sizeOfBlocks = []

for i in range(n):
    for j in range(n):
        k = grid[i][j]
        if canGo(i,j,k):
            sizeOfBlocks.append(1)
            visited[i][j] = True
            dfs(i, j,k)

# print(sizeOfBlocks)

blowingBlocks = 0
for l in sizeOfBlocks:
    if l >= 4:
        blowingBlocks += 1
maxBlock = max(sizeOfBlocks)

print(blowingBlocks, maxBlock)