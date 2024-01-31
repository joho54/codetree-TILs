from collections import deque
#input


n, m = tuple(map(int, input().split()))
grid = [
    list(map(int, input().split()))
    for _ in range(n)
]
meltList = []

q = deque()

def push(x,y):
    visited[x][y] = True
    q.append([x,y])

def inRange(x, y):
    return x >= 0 and x < n and y >= 0 and y < m

def canGo(x, y):
    if inRange(x, y) and not visited[x][y] and grid[x][y] != 1:
        return True
    return False

def addMeltList(x, y):
    global meltList
    dxs = [0, 0, -1, 1]
    dys = [1, -1, 0, 0]
    for dx, dy in zip(dxs, dys):
        nx, ny = x+dx, y+dy
        if inRange(nx, ny) and grid[nx][ny] == 1 and not [nx,ny] in meltList:
            meltList.append([nx, ny])

def bfs():
    dxs = [0, 0, -1, 1]
    dys = [1, -1, 0, 0]
    
    while q:
        x, y = q.popleft()
        for dx, dy in zip(dxs, dys):
            new_x, new_y = x+dx, y+dy
            if canGo(new_x,new_y):
                addMeltList(new_x,new_y)
                visited[new_x][new_y] = True
                push(new_x, new_y)

def printGrid(grid):
    for g in grid:
        print(g)
    print('----------')
t= 0
isIced = True
while isIced:
    sumVal = 0
    visited = [[False for _ in range(m)]for _ in range(n)]
    meltList = []
    push(0,0)
    bfs()
    for x, y in meltList:
        grid[x][y] = 0

    for e in grid:
        sumVal += sum(e)    
    if sumVal == 0: isIced = False

    #printGrid(grid)
    tmp = len(meltList)
    t+= 1
# print("--------")
# print(meltList)
print(t, len(meltList))