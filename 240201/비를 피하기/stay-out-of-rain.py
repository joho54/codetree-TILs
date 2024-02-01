#0: empty
#1: wall
#2: man
#3: destination.

from collections import deque

#input
n, h, m = tuple(map(int, input().split()))

grid = [
    tuple(map(int, input().split()))
    for _ in range(n)
]

manLoc = []

for i in range(n):
    for j in range(n):
        if grid[i][j] == 2:
            manLoc.append([i,j])

#bfs






def push(x,y, s):
    visited[x][y] = True
    step[x][y] = s
    q.append([x,y])

def inRange(x, y):
    return x >= 0 and x < n and y >= 0 and y < n

def canGo(x, y):
    if inRange(x, y) and not visited[x][y] and grid[x][y] != 1: 
        return True
    return False

aStep = 0
def bfs():
    global aStep
    dxs = [-1,1,0,0]
    dys = [0,0,1,-1]
    
    while q:
        x, y = q.popleft()
        if grid[x][y] == 3:
            aStep = step[x][y]
            q.clear()
            break
        #if found 3
        for dx, dy in zip(dxs, dys):
            new_x, new_y = x+dx, y+dy
            if canGo(new_x,new_y):
                visited[new_x][new_y] = True
                push(new_x, new_y, step[x][y]+1)
                # print(new_x, new_y)

q = deque()
ans = [[0 for _ in range(n)] for _ in range(n)]
for man in manLoc:
    visited = [[False for _ in range(n)] for _ in range(n)]
    #reset step here. 
    aStep = 0
    step = [[0 for _ in range(n)] for _ in range(n)]
    r, c = man
    # print('man', r,c)
    push(r,c, 0)
    bfs()
    # print('------',aStep)    
    ans[r][c] = aStep
    if aStep == 0:
        ans[r][c] = -1

for e in ans:
    for ee in e:
        print(ee, end = ' ')
    print()