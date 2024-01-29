#인접 행렬 사용
n, m = tuple(map(int, input().split()))
edges = [
    sorted(tuple(map(int, input().split())))
    for _ in range(m)
]

visited = [False]*(n+1)
global ans
ans = 0
def dfs(vertex):
    global ans
    for curr_v in range(1, n+1):
        if graph[vertex][curr_v] and not visited[curr_v]:
            visited[curr_v] = True
            dfs(curr_v)
            ans += 1

#graph record
graph = [[0 for _ in range(n+1)] for _ in range(n+1)]
for x, y in edges:
    graph[x][y] = 1
# for g in graph:
#     print(g)
root = 1
dfs(root)
print(ans)