#인접 행렬 사용
n, m = tuple(map(int, input().split()))
edges = [
    (tuple(map(int, input().split())))
    for _ in range(m)
]

visited = [False for _ in range(n+1)]
global ans
ans = 0
def dfs(vertex):
    global ans
    for curr_v in range(1, n+1):
        if graph[vertex][curr_v] and not visited[curr_v]:
            visited[curr_v] = True
            ans += 1
            # print("entering:", curr_v)
            dfs(curr_v)

def dfs_byAdjacancyList(vertex):
    global ans
    for curr_v in adjacancyList[vertex]:
        if not visited[curr_v]:
            visited[curr_v] = True
            ans += 1
            # print("entering:", curr_v)
            dfs_byAdjacancyList(curr_v)

#graph record
graph = [[0 for _ in range(n+1)] for _ in range(n+1)]
adjacancyList = [[] for _ in range(n+1)]
for x, y in edges:
    graph[x][y] = 1
    graph[y][x] = 1
for x, y in edges:
    adjacancyList[x].append(y)
    adjacancyList[y].append(x)
# for g in graph:
#     print(g)
root = 1
visited[root]= True
dfs_byAdjacancyList(root)
print(ans)