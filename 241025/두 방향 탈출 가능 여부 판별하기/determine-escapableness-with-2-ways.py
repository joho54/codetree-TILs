# 모든 그리드 문제는 그래프다.

dxs = [1, 0]
dys = [0, 1]

# input
n, m = tuple(map(int, input().split()))
grid = [
    tuple(map(int, input().split()))
    for _ in range(n)
]

visited = [[False for _ in range(m)] for _ in range(n)]

def in_range(x, y):
    return x >= 0 and x < n and y >= 0 and y < m

flag = False

def dfs(x, y):
    global flag
    if (x, y) == (n-1, m-1): 
        flag = True
        print("we got it")
        return
    # base condition? no new x, y
    no_visit = True
    # get new_x, new_y
    for dx, dy in zip(dxs, dys):
        new_x = x + dx
        new_y = y + dy
        # not visited, no snake. if we can visit, what?
        if in_range(new_x, new_y) and not visited[new_x][new_y] and grid[new_x][new_y] == 1:
            # recursion
            visited[new_x][new_y] = True
            dfs(new_x, new_y)
            # print("visiting:", new_x, new_y)
            no_visit = False
    if no_visit:
        return

visited[0][0] = 1
dfs(0, 0)

if flag: print(1)
else: print(0)


# adjacency matrix
# adjacency list
# 필요 없다. 왜? 그리드가 그래프라서. (인접행렬인 셈이다.)