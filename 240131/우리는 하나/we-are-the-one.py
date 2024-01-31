from collections import deque
import copy

n, k, u, d = tuple(map(int, input().split()))
#canGo
grid = [
    tuple(map(int, input().split()))
    for _ in range(n)
]

q = deque()

ans = 0
maxAns = 0

def push(x,y):
    visited[x][y] = True
    q.append([x,y])

def inRange(x, y):
    return x >= 0 and x < n and y >= 0 and y < n

def canGo(x, y, curr_height):
    if inRange(x, y) and not visited[x][y]:   
        heightD = abs(grid[x][y]-curr_height)
        if heightD >= u and heightD <= d:
            return True
    return False

def bfs():
    ans = 1
    dxs = [0, 0, -1, 1]
    dys = [1, -1, 0, 0]
    
    while q:
        x, y = q.popleft()
        curr_height = grid[x][y]
        for dx, dy in zip(dxs, dys):
            new_x, new_y = x+dx, y+dy
            if canGo(new_x,new_y, curr_height):
                visited[new_x][new_y] = True
                push(new_x, new_y)
                ans += 1
                #print(new_x, new_y)
    return ans


visited = [[False for _ in range(n)] for _ in range(n)]

def recursiveSim(li, lj, cityList):
    global visited
    global ans 
    global maxAns
    if len(cityList) == k:
        ans = 0

        visited = [[False for _ in range(n)] for _ in range(n)]
        for x, y in cityList:
            push(x, y)
            ans += bfs()
        if maxAns < ans:
            maxAns = ans
        return

    for i in range(li, n):
        for j in range(lj, n):
            if not [i,j] in cityList:
                cityList.append([i,j])
                #print('city list ',cityList)
                recursiveSim(i,j, cityList)
                cityList.pop()

recursiveSim(0,0,[])
print(maxAns)