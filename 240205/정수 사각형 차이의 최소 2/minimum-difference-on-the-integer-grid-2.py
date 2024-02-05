import sys

INT_MAX = sys.maxsize
MAX_R = 100

# 변수 선언 및 입력:
n = int(input())
num = [
    list(map(int, input().split()))
    for _ in range(n)
]
dp = [
    [0] * n
    for _ in range(n)
]

ans = INT_MAX

def initialize():
    # 전부 INT_MAX로 초기화합니다.
    for i in range(n):
        for j in range(n):
            dp[i][j] = INT_MAX

    # 시작점의 경우 dp[0][0] = num[0][0]으로 초기값을 설정해줍니다
    dp[0][0] = num[0][0]

    # 최좌측 열의 초기값을 설정해줍니다.
    for i in range(1, n):
        dp[i][0] = max(dp[i - 1][0], num[i][0])

    # 최상단 행의 초기값을 설정해줍니다.
    for j in range(1, n):
        dp[0][j] = max(dp[0][j - 1], num[0][j])


def solve(lower_bound):
    # lower_bound 미만의 값은 사용할 수 없도록
    # num값을 변경해줍니다.
    for i in range(n):
        for j in range(n):
            if num[i][j] < lower_bound:
                num[i][j] = INT_MAX
    
    # DP 초기값 설정
    initialize()

    # 탐색하는 위치의 위에 값과 좌측 값 중에 작은 값과
    # 해당 위치의 숫자 중에 최댓값을 구해줍니다.
    for i in range(1, n):
        for j in range(1, n):
            dp[i][j] = max(min(dp[i - 1][j], dp[i][j - 1]), num[i][j])
        
    return dp[n - 1][n - 1]

   
# 최솟값을 k라고 가정했을 때
# lower_bound 이상의 수들만 사용하여 
# 이동한다는 조건하에서
# 최댓값을 최소로 만드는 DP 문제를 풀어줍니다.
for lower_bound in range(1, MAX_R + 1):
    upper_bound = solve(lower_bound)
    
    # 다 진행했음에도 여전히 INT_MAX라면 
    # 그러한 이동이 불가능하다는 뜻이므로
    # 패스합니다.
    if upper_bound == INT_MAX:
        continue
    
    # 답을 갱신합니다.
    ans = min(ans, upper_bound - lower_bound)

print(ans)