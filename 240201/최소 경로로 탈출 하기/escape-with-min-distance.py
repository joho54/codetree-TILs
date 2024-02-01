from collections import deque

#input
n, m = tuple(map(int, input().split()))

grid = [
    tuple(map(int, input().split()))
    for _ in range(n)
]

#bfs
q = deque()

visited = [[False for _ in range(m)] for _ in range(n)]
step = [[0 for _ in range(m)] for _ in range(n)]


def push(x,y, s):
    visited[x][y] = True
    step[x][y] = s
    q.append([x,y])

def inRange(x, y):
    return x >= 0 and x < n and y >= 0 and y < m

def canGo(x, y):
    if inRange(x, y) and not visited[x][y] and grid[x][y] != 0: 
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

push(0,0, 0)
bfs()

if step[n-1][m-1] == 0:
    print(-1)
else: print(step[n-1][m-1])