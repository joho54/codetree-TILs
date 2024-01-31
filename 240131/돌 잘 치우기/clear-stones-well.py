from collections import deque
import copy
movedStonsList = []

n, k, m = tuple(map(int, input().split()))
grid = [
    list(map(int, input().split()))
    for _ in range(n)
]
stoneList = []
for i in range(n):
    for j in range(n):
        if grid[i][j] == 1:
            stoneList.append([i,j])

startPs = []
q = deque()

maxAns = 0

def recursivelySearch(ls, movedStonsList):
    global maxAns
    #base condition: if we removed mth stone, we do bfs
    if len(movedStonsList) == m:
        ans = 0
        # print('moved stones',movedStonsList)
        # print('recursion end')
        visited = [[False for _ in range(n)] for _ in range(n)]
        simGrid = copy.deepcopy(grid)
        for s in movedStonsList:
            simGrid[s[0]][s[1]] = 0
        #printGrid(simGrid)
        for p in startPs:
            r, c = p[0], p[1]
            if not visited[r][c]:
                push(r,c, visited)
                # print('starting point:', r, c)
                ans += bfs(simGrid, visited)
                # print("---another starting point-----")
                if maxAns < ans:
                    maxAns = ans
        return    
    #recursion
    #here we remove stons recursively.
    l = len(stoneList)
    for st in range(ls+1, l):
        i, j = stoneList[st]
        if not [i,j] in movedStonsList:
            movedStonsList.append([i,j])
            recursivelySearch(st, movedStonsList)
            movedStonsList.pop()

# def printGrid(arr):
#     for e in arr:
        # print(e)
    # print("===========")


for _ in range(k):
    r, c = tuple(map(int, input().split()))
    startPs.append([r-1, c-1])

def push(x,y, visited):
    visited[x][y] = True
    q.append([x,y])

def inRange(x, y):
    return x >= 0 and x < n and y >= 0 and y < n

def canGo(x, y, simGrid, visited):
    if inRange(x, y) and not visited[x][y] and simGrid[x][y] != 1:
        return True
    return False
    
def bfs(simGrid, visited):
    dxs = [0, 1, -1, 0]
    dys = [1, 0, 0, -1]
    ans = 1
    while q:
        x, y = q.popleft()
        for dx, dy in zip(dxs, dys):
            new_x, new_y = x+dx, y+dy
            if canGo(new_x,new_y, simGrid, visited):
                visited[new_x][new_y] = True
                push(new_x,new_y, visited)
                # print(new_x,new_y)
                ans += 1
    return ans
                

recursivelySearch(-1, movedStonsList)
print(maxAns)