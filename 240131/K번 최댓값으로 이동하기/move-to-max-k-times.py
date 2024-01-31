from collections import deque

#input
n, k = tuple(map(int, input().split()))

grid = [
    tuple(map(int, input().split()))
    for _ in range(n)
]

r, c = tuple(map(int, input().split()))
r, c = r-1,c-1

q = deque()


def push(x,y):
    visited[x][y] = True
    q.append([x,y])


def inRange(x, y):
    return x >= 0 and x < n and y >= 0 and y < n

def canGo(x, y, keyVal):
    if inRange(x, y) and not visited[x][y] and keyVal > grid[x][y]:
        return True
    return False
    
# x is key val
def bfs(keyVal):
    dxs = [1, 0, 0, -1] # down, right, left, up
    dys = [0, 1, -1, 0]
    currP = [-1,-1,-1]  #val, x, y
    while q:
        x, y = q.popleft()
        for dx, dy in zip(dxs, dys):
            new_x, new_y = x+dx, y+dy
            if canGo(new_x, new_y, keyVal):
                if currP[0] <= grid[new_x][new_y]:
                    currP = [grid[new_x][new_y], new_x, new_y]
                    # print(currP)
                # print(new_x, new_y)
                push(new_x, new_y)
    return currP



#have to set nexts starting point. this time we need other conditions.


for _ in range(k):
    # print('------------------')
    visited = [[False for _ in range(n)] for _ in range(n)]
    push(r,c)
    keyVal = grid[r][c]
    v, r, c = bfs(keyVal)
    if v == -1:
        break

print(r+1, c+1)