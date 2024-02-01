from collections import deque

#input
n, k = tuple(map(int, input().split()))

grid = [
    tuple(map(int, input().split()))
    for _ in range(n)
]

#bfs
q = deque()

visited = [[False for _ in range(n)] for _ in range(n)]
step = [[0 for _ in range(n)] for _ in range(n)]

rottenList = []

for i in range(n):
    for j in range(n):
        if grid[i][j] == 2:
            rottenList.append([i,j])


def push(x,y, s):
    visited[x][y] = True
    step[x][y] = s
    q.append([x,y])

def inRange(x, y):
    return x >= 0 and x < n and y >= 0 and y < n

def canGo(x, y):
    if inRange(x, y) and not visited[x][y] and grid[x][y] == 1: 
        return True
    return False


def bfs():
    dxs = [0, 0, -1, 1]
    dys = [1, -1, 0, 0]
    
    while q:
        x, y = q.popleft()
        for dx, dy in zip(dxs, dys):
            new_x, new_y = x+dx, y+dy
            if canGo(new_x,new_y):
                visited[new_x][new_y] = True
                push(new_x, new_y, step[x][y]+1)

for x, y in rottenList:
    visited = [[False for _ in range(n)] for _ in range(n)]
    push(x,y, 0)
bfs()

ans = [[-1 for _ in range(n)] for _ in range(n)]
for i in range(n):
    for j in range(n):
        if grid[i][j] == 1 and step[i][j] > 0:
            ans[i][j] = step[i][j]
        elif grid[i][j] == 1 and step[i][j] == 0:
            ans[i][j] = -2
        elif grid[i][j] == 2:
            ans[i][j] = 0

for s in ans:
    for ss in s:
        print(ss, end = ' ')
    print()