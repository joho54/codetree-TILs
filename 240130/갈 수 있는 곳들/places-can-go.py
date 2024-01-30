from collections import deque

n, k = tuple(map(int, input().split()))

grid = [
    tuple(map(int, input().split()))
    for _ in range(n)
]

moves = []

for _ in range(k):
    r, c = tuple(map(int, input().split()))
    moves.append([r-1, c-1])

visited = [[False for _ in range(n)] for _ in range(n)]
q = deque()

#canGo: 

def canGo(x, y):
    if inRange(x, y) and grid[x][y] != 1 and not visited[x][y]:
        return True
    else: False

def push(x, y):
    visited[x][y] = True
    q.append([x,y])

def inRange(x, y):
    return x >= 0 and x < n and y >= 0 and y < n


ans = 0

def bfs():
    global ans
    dxs = [0, 1, 0, -1]
    dys = [1, 0, -1, 0]
    while q:
        x, y = q.popleft()
        for dx, dy in zip(dxs, dys):
            new_x, new_y = x+dx, y+dy
            if canGo(new_x, new_y):
                ans += 1
                # print(new_x, new_y)
                push(new_x, new_y)



for ms in moves:
    r, c = ms
    ans += 1
    push(r,c)


bfs()
print(ans)