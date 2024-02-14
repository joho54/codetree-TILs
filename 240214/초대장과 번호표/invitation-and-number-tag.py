from collections import deque
q = deque()

#input
n, g = tuple(map(int, input().split()))
groups = [
    tuple(map(int, input().split()))
    for _ in range(g)
]
invitedOnes = set()
invitedOnes.add(1)
q.append(1)
groupSorted = []

while q:
    _ = q.popleft()
    for details in groups:
        groupList = []
        groupSize = details[0]
        for i in range(1, groupSize+1):
            groupList.append(details[i])
        # print(groupList)
        invitedNums = 0

        #what is g? 1, 3 ,...
        for g in groupList:
            if g in invitedOnes:
                invitedNums += 1
                # print('invited!!', g)
            else:
                uninvited = g
                # print('uninvited!!', uninvited)
        if invitedNums == groupSize-1:
            q.append(uninvited)
            invitedOnes.add(uninvited)

            # print('so we invited', uninvited)
                
print(len(invitedOnes))