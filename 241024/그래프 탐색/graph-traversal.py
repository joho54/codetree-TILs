n, m = tuple(map(int, input().split()))

#adjacency matrix
graph = [[0 for _ in range(n+1)] for _ in range(n+1)]
graph2 = [[] for _ in range(n+1)]
visited = [0 for _ in range(n+1)]
visited2 = [0 for _ in range(n+1)]


for _ in range(m):
    x, y = tuple(map(int, input().split()))
    graph[x][y] = 1
    graph[y][x] = 1

    graph2[x].append(y)
    graph2[y].append(x)


def dfs_adjacent_matrix(vertex):
    # if it's not visted and edge exist
    for curr_v in range(1, n+1):
        if graph[vertex][curr_v] == 1 and visited[curr_v] == 0:
            visited[curr_v] = 1
            dfs_adjacent_matrix(curr_v)

def dfs_adjacent_list(vertex):
    for curr_v in graph2[vertex]:
        if visited2[curr_v] == 0:
            visited2[curr_v] = 1
            dfs_adjacent_list(curr_v)
    
    

dfs_adjacent_list(1)

print(sum(visited2)-1 if sum(visited2)-1 >= 0 else 0)