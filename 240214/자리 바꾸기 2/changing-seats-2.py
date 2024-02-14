#input
n, k = tuple(map(int, input().split()))

changeList = [
    tuple(map(int, input().split()))
    for _ in range(k)
]

ls = []
seats = []
for i in range(n):
    tmp = set()
    ls.append(tmp)
    seats.append(i+1)
#now we have list of sets.
# print(seats)
#set sets. lol
for i in range(n):
    ls[i].add(i+1)
# print(ls)
for _ in range(3):
    for a, b in changeList:
        #change people of a and b
        #change real data.
        tmp = seats[a-1]
        seats[a-1] = seats[b-1]
        seats[b-1] = tmp

        #update sets.
        #for person at a
        #this is set. add current seat
        ls[seats[a-1]-1].add(a)
        ls[seats[b-1]-1].add(b)

for e in ls:
    print(len(e))