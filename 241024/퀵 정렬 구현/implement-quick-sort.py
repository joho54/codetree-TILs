# second form
def quick_sort2(A, first, last):
    # base condition
    if first >= last: return
    # set pointers
    smaller, equal, larger = first, first, last+1
    # set pivot
    pivot = A[first]
    # then what? go to while
    while equal < larger:
        # for every condition of equal
        if A[equal] == pivot:
            # just increment equal
            equal += 1
            
        elif A[equal] < pivot:
            # change this with smaller and decrement smaller pointer
            A[equal], A[smaller] = A[smaller], A[equal]
            equal += 1
            smaller += 1
        
        elif A[equal] > pivot:
            # change this with larger and decrement smaller pointer
            larger -= 1
            A[equal], A[larger] = A[larger], A[equal]
    # now recursion
    quick_sort2(A, first, smaller-1)
    quick_sort2(A, larger, last)

def quick_sort3(A):
    # base condition
    if len(A) <= 1: return A
    S, M, L = [], [], []
    pivot = A[0]

    for e in A:
        if e < pivot:
            S.append(e)
        elif e > pivot:
            L.append(e)
        elif e == pivot:
            M.append(e)
    return quick_sort3(S) + M + quick_sort3(L)

    
n = int(input())

arr = list(map(int, input().split()))

# quick_sort2(arr, 0, len(arr)-1)

arr_sorted = quick_sort3(arr)

for x in arr_sorted:
    print(x, end=" ")