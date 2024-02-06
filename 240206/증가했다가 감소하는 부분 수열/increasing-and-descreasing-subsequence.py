#input
n = int(input())

arr = tuple(map(int, input().split()))

#two dps
dp_increase = [0 for _ in range(n)]
dp_decrease = [0 for _ in range(n)]

#setup: list, starting idx, ending idx
dp_increase[0] = [1, 0, 0]
dpList1, dpList2 = [[1, 0, 0]], [[1, 0, 0]]
dp_decrease[0] = [1, 0, 0]

for i in range(1, n):
    for j in range(0, i):
        #수열이 언제 시작하는지는 상관 없음. 언제 끝나는지가 중요함
        if arr[j] < arr[i]: #this is where update happens
            dp_increase[i] = [dp_increase[j][0]+1, dp_increase[j][1], i]
            if not dp_increase[i] in dpList1:  
                dpList1.append(dp_increase[i])
        else:
            dp_increase[i] = [1, i, i]
            if not dp_increase[i] in dpList1:  
                dpList1.append(dp_increase[i])

        #수열이 언제 끝나는지는 상관 없음. 언제 시작되는지가 중요함. 그런가?
        if arr[j] > arr[i]: #this is where update happens
            dp_decrease[i] = [dp_decrease[j][0]+1, dp_decrease[j][1], i]
            if not dp_decrease[i] in dpList2: 
                dpList2.append(dp_decrease[i])
        else:
            dp_decrease[i] = [1, i, i]
            if not dp_decrease[i] in dpList2: 
                dpList2.append(dp_decrease[i])
ans = []

#O(n^2)
for i in range(len(dpList1)):
    for j in range(len(dpList2)):
        if dpList1[i][2] < dpList2[j][1]:
            ans.append(dpList1[i][0]+dpList2[j][0])     
        elif dpList1[i][2] == dpList2[j][1]:
            ans.append(dpList1[i][0]+dpList2[j][0]-1)
# print(dpList1)
# print(dpList2)

print(max(ans))