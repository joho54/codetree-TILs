n, m = tuple(map(int, input().split()))
#visited
visited = [[False for _ in range(m)] for _ in range(n)]

#grid record
grid = [
    tuple(map(int, input().split()))
    for _ in range(n)
]

def inRange(x, y):
    return x >= 0 and x < n and y >= 0 and y < m

def canGo(x, y):
    #if there is no snake, and in range, and not visited
    if inRange(x,y) and grid[x][y] != 0 and not visited[x][y]:
        return True
    return False
                
def dfs(x, y):
    #dx, dy
    dxs = [0, 1]
    dys = [1, 0]    
    for dx, dy in zip(dxs, dys):
        new_x, new_y = x+dx, y+dy
        if canGo(new_x, new_y):
            visited[new_x][new_y] = True
            dfs(new_x, new_y)

dfs(0, 0)
if visited[n-1][m-1]:
    print(1)
else:
    print(0)