#it's another sort of dx, dy
#instead, we have [0, -1, 1] in plus list, [1, 2, 3] in divide list
#but every step is equal. so how do I do equal?
#
#if it's devidable, set dxs =[2] or dxs = [3]. otherwise [-1, 1]. 
#then iterate.

from collections import deque
q = deque()

# i realized how to set visited

N = int(input())
visited = [False for _ in range(N+4)]
step = [0 for _ in range(N+4)]

def canGo(n, dx): 
    if n < N+2 and not visited[n] and n >= 1:
        return True
    return False

def operate(n, dx):
    if dx == 2 or dx == 3:
        if n%dx == 0:
            return n//dx
        else: n
    return n+dx


def push(new_n, s):
    visited[new_n] = True
    q.append(new_n)
    step[new_n] = s

ans =0 
def bfs():
    global ans
    dxs = [-1, 1, 2,3]
    while q:
        num = q.popleft()
        tmp = num
        # print("current step", num, step[num])
        for dx in dxs:
            num = tmp
            new_N = operate(num, dx)
            if canGo(new_N,dx):
                # print('num has to be fixed', num)   
                # print('push val', new_N, step[num]+1)
                push(new_N, step[num]+1)
    # print('-----------------')
    if visited[1] != 0:
        ans = step[1]
    else: ans = -1

push(N, 0)            
bfs()
print(ans)