from collections import deque

#input
n = int(input())
r1, c1, r2, c2 = tuple(map(int, input().split()))
r1, c1, r2, c2 = r1-1, c1-1, r2-1, c2-1

#grid = [[0 for _ in range(n)]for _ in range(n)]

#bfs
q = deque()

visited = [[False for _ in range(n)] for _ in range(n)]
step = [[0 for _ in range(n)] for _ in range(n)]


def push(x,y, s):
    visited[x][y] = True
    step[x][y] = s
    q.append([x,y])

def inRange(x, y):
    return x >= 0 and x < n and y >= 0 and y < n

def canGo(x, y):
    if inRange(x, y) and not visited[x][y]: 
        return True
    return False


def bfs():
    dxs = [-1, -2, -2, -1, 1, 2, 2, 1]
    dys = [-2, -1, 1, 2, 2, 1, -1, -2]
    
    while q:
        x, y = q.popleft()
        for dx, dy in zip(dxs, dys):
            new_x, new_y = x+dx, y+dy
            if canGo(new_x,new_y):
                visited[new_x][new_y] = True
                push(new_x, new_y, step[x][y]+1)

push(r1,c1, 0)
bfs()

if step[r2][c2] == 0:
    print(-1)
else: print(step[r2][c2])