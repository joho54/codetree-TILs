n = int(input())
UNUSED = -1
memo = [UNUSED for _ in range(n+1)]

#재귀 내부 함수는 level
def recur(level):
    #memoization
    if memo[level] != UNUSED:
        return memo[level]
    #base conditions
    if level == 0:
        memo[level]=0
        return memo[level]
    if level == 1:
        memo[level] = 1
        return memo[level]
    if level == 2:
        memo[level] = 2
        return memo[level]
    if level == 3:
        memo[level] =3
        return memo[level]
    

    
    
    memo[level] = recur(level-1)+recur(level-2)
    return memo[level]

print(recur(n)%10007)
# print(memo)