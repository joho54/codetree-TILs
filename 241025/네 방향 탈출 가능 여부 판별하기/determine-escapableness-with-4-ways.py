# we need four function for bfs problem

from collections import deque

q = deque()
# input
n, m = tuple(map(int, input().split()))

dxs = [1, -1, 0, 0]
dys = [0, 0, 1, -1]

grid = [
    tuple(map(int, input().split()))
    for _ in range(n)
]

visited = [
    [False for _ in range(m)]
    for _ in range(n)
]

def can_go(x, y):
    # is grid exist? and not visited?
    if in_range(x, y) and grid[x][y] == 1 and not visited[x][y]:
        return True

def in_range(x, y):
    return x >= 0 and x < n and y >= 0 and y < m

def push(x, y):
    visited[x][y] = True
    q.append((x, y))
    
    
is_out = False

def bfs():
    global is_out
    while q:
        x, y = q.popleft()
        if (x, y) == (n-1, m-1): 
            is_out = True
            return
        for dx, dy in zip(dxs, dys):
            new_x = x + dx
            new_y = y + dy
            if can_go(new_x, new_y):
                push(new_x, new_y)

q.append((0, 0))
bfs()

if is_out: print(1)
else: print(0)