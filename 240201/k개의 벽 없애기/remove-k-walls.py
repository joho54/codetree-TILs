#recursively pick.
#we need wall list

from collections import deque
import copy
import sys

INT_MAX = sys.maxsize
wallList = []

#input
n, k = tuple(map(int, input().split()))
visited = [[False for _ in range(n)]for _ in range(n)]
grid = [
    list(map(int, input().split()))
    for _ in range(n)
]

r1,c1 = tuple(map(int, input().split()))
r2, c2 = tuple(map(int, input().split()))
r1, c1, r2, c2 = r1-1, c1-1, r2-1, c2-1

#set wall list for backtracking
for i in range(n):
    for j in range(n):
        if grid[i][j] == 1:
            wallList.append([i,j])

#recursion


def push(x,y, s):
    global visited, step
    visited[x][y] = True
    step[x][y] = s
    q.append([x,y])

def inRange(x, y):
    return x >= 0 and x < n and y >= 0 and y < n

def canGo(x, y, simGrid):
    global visited
    if inRange(x, y) and not visited[x][y] and simGrid[x][y] != 1: 
        return True
    return False

def bfs(simGrid):
    global visited, step, stepVal, minStepVal
    dxs = [-1,1,0,0]
    dys = [0,0,1,-1]
    
    while q:
        x, y = q.popleft()
        #if reached location
        if (x,y) == (r2, c2):
            stepVal = step[r2][c2]
            if stepVal < minStepVal:
                minStepVal = stepVal
                # print("min step val",minStepVal)
            q.clear()
            # gridOutput(simGrid)
            # print("found===========")
            break
        for dx, dy in zip(dxs, dys):
            new_x, new_y = x+dx, y+dy
            if canGo(new_x,new_y, simGrid):
                visited[new_x][new_y] = True
                push(new_x, new_y, step[x][y]+1)
                # print(new_x, new_y)
def gridOutput(grid):
    for g in grid:
        print(g)

q = deque()
step = [[0 for _ in range(n)]for _ in range(n)]
stepVal, minStepVal = 0, INT_MAX
def recurSearch(idx, removedWallList):
    global stepVal, minStepVal, visited, step

    #base condition
    if len(removedWallList) == k:
        #sim
        simGrid = copy.deepcopy(grid)
        visited = [[False for _ in range(n)]for _ in range(n)]
        step = [[0 for _ in range(n)]for _ in range(n)]
        #removed wall
        for x, y in removedWallList:
            simGrid[x][y] = 0
        #gridOutput(simGrid)
        push(r1, c1,0)
        #bfs
        bfs(simGrid)
        

    #recursion
    #idx is preveiously chosen i
    for i in range(idx+1, len(wallList)):
        removedWallList.append(wallList[i])
        recurSearch(i, removedWallList)
        removedWallList.pop()

recurSearch(-1, [])

if minStepVal == INT_MAX:
    print(-1)
else: print(minStepVal)