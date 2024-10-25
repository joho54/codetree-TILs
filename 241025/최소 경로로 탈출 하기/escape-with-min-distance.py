# 최소경로로 탈출하기 문제는 가중치가 동일한 그래프에서의 BFS와 같다.

from collections import deque

dxs = [0, 0, -1, 1]
dys = [1, -1, 0, 0]

q = deque()
# 4 functions. push, in_range, can_go, bfs
# 3 vars. grid, visited, steps, 


# input
n, m = tuple(map(int, input().split()))
grid = [
    tuple(map(int, input().split()))
    for _ in range(n)
]

visited = [
    [False for _ in range(m)]
    for _ in range(n)
]

steps = [
    [-1 for _ in range(m)] # is it right to set 0?
    for _ in range(n)
]

def push(x, y, s):
    visited[x][y] = True
    steps[x][y] = s
    q.append((x, y, s))

def can_go(x, y):
    if in_range(x, y):
        if not visited[x][y] and grid[x][y] == 1:
            return True
    return False

def in_range(x, y):
    return x >= 0 and x < n and y >= 0 and y < m

def bfs():
    while q:
        x, y, s = q.popleft()
        for dx, dy in zip(dxs, dys):
            new_x = x + dx
            new_y = y + dy

            if can_go(new_x, new_y):
                push(new_x, new_y, s + 1)

q.append((0, 0, 0))

bfs()

print(steps[n-1][m-1])