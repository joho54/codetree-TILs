# 무식한 방법: 합치고 정렬한다.
# 덜 무식한 방법: 합치고 합친 하나의 값만 이진 정렬로? 한번 해봐 뭐

n = int(input())
nums = list(map(int, input().split()))

# nums.sort()
ans = 0

while len(nums) > 1: # until there are 2 elements
    minA = min(nums)
    idxA = nums.index(minA)
    del nums[idxA]
    minB = min(nums)
    idxB = nums.index(minB)
    
    nums[idxB] = minA + minB
    ans += nums[idxB]

    # print(minA, minB)

print(ans)