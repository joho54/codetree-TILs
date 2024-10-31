# 음수가 되는 순간 끊기. 합을 계속 갱신하다가, 

# 입력
n = int(input())
arr = tuple(map(int, input().split()))
ans = 0
final_ans = 0

for a in arr:
    if ans+a > 0:
        ans += a
    else: 
        ans = a
    final_ans = max(ans, final_ans)

print(final_ans)