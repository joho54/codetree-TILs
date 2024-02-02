n = int(input())

memo = [-1 for _ in range(n+1)]

#level of stair
def recur(level):
    #memoization
    if memo[level] != -1:
        print('memo catched')
        return memo[level]
        
    #base condition
    if level == 0 or level == 1:
        return 0
    elif level == 2 or level == 3:
        return 1
        
    memo[level] = recur(n-2) + recur(n-3)
    
    return memo[level]

ans = recur(n)
print(ans%10007)