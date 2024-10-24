n, m = tuple(map(int, input().split()))

#adjacency matrix
graph = [[0] * (n+1)] *(n+1)
visited = [False] * (n+1)

for _ in range(m):
    x, y = tuple(map(int, input().split()))
    graph[x][y] = 1



def dfs(vertex):
    # if it's not visted and edge exist

    for curr_v in range(1, n+1):
        if graph[vertex][curr_v] == 1 and not visited[vertex]:
            visited[vertex] = True
            dfs(curr_v)



dfs(1)

print(sum(visited))