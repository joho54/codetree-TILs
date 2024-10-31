# 무식한 방법: 합치고 정렬한다.
# 덜 무식한 방법: 합치고 합친 하나의 값만 이진 정렬로? 한번 해봐 뭐

n = int(input())
nums = list(map(int, input().split()))

nums.sort()
ans = 0

while len(nums) > 1: # until there are 2 elements
    new_num = nums[0] + nums[1]
    ans += new_num
    # 이진 정렬 어떻게 하더라? 포인터 하나 가지고, 인덱스를 계속 갱신 하는데
    # 언제까지 갱신하지? 양쪽 값이 nums[idx] 사이가 될 때?
    # 종료 조건은 그거고, idx 감소 조건, 증가 조건도 따로지. 증가, 감소는 각각 어떻게 하지?
    # 감소: 기존 idx//2
    # 증가: 기존 int(idx*(1.5))
    #그냥 뮤식하게 소트하자..
    del nums[0]
    nums[0] = new_num
    nums.sort()


print(ans)