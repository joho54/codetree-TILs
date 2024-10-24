n, m = tuple(map(int, input().split()))

#adjacency matrix
graph = [[0 for _ in range(n+1)] for _ in range(n+1)]
visited = [0 for _ in range(n+1)]

for _ in range(m):
    x, y = tuple(map(int, input().split()))
    graph[x][y] = 1
    graph[y][x] = 1

def dfs(vertex):
    # if it's not visted and edge exist
    for curr_v in range(1, n+1):
        if graph[vertex][curr_v] == 1 and visited[curr_v] == 0:
            visited[curr_v] = 1
            dfs(curr_v)
            



dfs(1)

print(sum(visited)-1)