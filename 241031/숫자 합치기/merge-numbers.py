# q
import heapq

n = int(input())
nums = list(map(int, input().split()))

pq = []

ans = 0

for elem in nums:
    heapq.heappush(pq, elem)


while len(pq) > 1: # until there are 2 elements
    x1 = heapq.heappop(pq)
    x2 = heapq.heappop(pq)
    cost = x1+x2
    ans += cost
    # print(ans, x1, x2)
    heapq.heappush(pq, cost)


print(ans)