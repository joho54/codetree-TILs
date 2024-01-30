from collections import deque

n, m = tuple(map(int, input().split()))

grid = [
    tuple(map(int, input().split()))
    for _ in range(n)
]

visited = [[False for _ in range(m)] for _ in range(n)]
q = deque()

#canGo: 

def canGo(x, y):
    if inRange(x, y) and grid[x][y] != 0 and not visited[x][y]:
        return True
    else: False

def push(x, y):
    visited[x][y] = True
    q.append([x,y])

def inRange(x, y):
    return x >= 0 and x < m and y >= 0 and y < n


found = False
def bfs():
    global found
    dxs = [0, 1, 0, -1]
    dys = [1, 0, -1, 0]
    while q:
        x, y = q.popleft()
        for dx, dy in zip(dxs, dys):
            new_x, new_y = x+dx, y+dy
            if canGo(new_x, new_y):
                if new_x == n-1 and new_y == m-1:
                    found = True
                push(new_x, new_y)

push(0,0)
bfs()
if found:
    print(1)
else:
    print(0)