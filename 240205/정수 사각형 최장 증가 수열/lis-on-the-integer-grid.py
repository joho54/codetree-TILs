# 변수 선언 및 입력:
n = int(input())
grid = [
    list(map(int, input().split()))
    for _ in range(n)
]
dp = [
    [0] * n
    for _ in range(n)
]

cells = []
ans = 0


def in_range(x, y):
    return 0 <= x and x < n and 0 <= y and y < n

   
# 각 칸에 적혀있는 정수값 기준으로
# 오름차순이 되도록 칸의 위치들을 정렬합니다.
# 편하게 정렬하기 위해
# (칸에 적혀있는 값, 행 위치, 열 위치) 순으로 넣어줍니다.
for i in range(n):
    for j in range(n):
        cells.append((grid[i][j], i, j))

# 오름차순으로 정렬을 진행합니다.
cells.sort()

# 처음 DP 값들은 전부 1로 초기화해줍니다. (해당 칸에서 시작하는 경우)
for i in range(n):
    for j in range(n):
        dp[i][j] = 1

# 정수값이 작은 칸부터 순서대로 보며
# 4방향에 대해 dp 값을 갱신해줍니다.
for _, x, y in cells:
    dxs, dys = [-1, 1, 0, 0], [0, 0, -1, 1]

    # 인접한 4개의 칸에 대해 갱신을 진행합니다.
    for dx, dy in zip(dxs, dys):
        nx, ny = x + dx, y + dy
        if in_range(nx, ny) and grid[nx][ny] > grid[x][y]:
            dp[nx][ny] = max(dp[nx][ny], dp[x][y] + 1)

# 전체 수들 중 최댓값을 찾습니다.
for i in range(n):
    for j in range(n):
        ans = max(ans, dp[i][j])

print(ans)