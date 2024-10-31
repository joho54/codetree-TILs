# 음수가 되는 순간 끊기. 합을 계속 갱신하다가, 

# 입력
n = int(input())
arr = tuple(map(int, input().split()))
ans = arr[0]
final_ans = arr[0]

for a in arr[1:]:
    # 만약 지금까지의 합이 0보다 작으면 끊는게 이득이다. 끊을 때 이렇게밖에 못 끊는다.
    if ans < 0: 
        ans = a
    else:
        ans += a
    final_ans = max(ans, final_ans)

print(final_ans)