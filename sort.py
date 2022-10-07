def selection_sort(A):
    for i in range(len(A)-1):
        minimum = i
        for j in range(i+1, len(A)):
            if A[j] < A[minimum]: minimum=j
        A[i],A[minimum]=A[minimum],A[i]

def insetion_sort(A):
    for i in range(1,len(A)):
        for j in range(i,0,-1):
            if A[j]<A[j-1]: A[j], A[j-1] = A[j-1], A[j]

def bubble_sort(A):
    n = len(A)
    for i in range(n-1, 0, -1):
        bChanged = False
        for j in range(i):
            if A[j]>A[j+1]:
                A[j], A[j+1] = A[j+1], A[j]
                bChanged = True
        if not bChanged: break

def shell_sort(A):
    n = len(A)
    gap = n//2
    while n>0:
        if (gap%2)==0: gap+=1
        for i in range(gap):
            sortGapInsertion(A, i, n-1, gap)
        gap = gap//2

def sortGapInsertion(A, first, last, gap):
    for i in range(first+gap, last+1, gap):
        key = A[i]
        j = i-gap
        while j >= first and A[j]>key:
            A[j+gap] = A[j]
            j -= gap
        A[j+gap] = key

def quick_sort(A, left, right):
    if left < right:
        q = partition(A, left, right)
        quick_sort(A, left, q-1)
        quick_sort(A, q+1, right)

def partition(A, left, right):
    low = left+1
    high = right
    pivot = A[left]
    while low <= high:
        while low <= right and A[low]<pivot: low += 1
        while high >= left and A[high]>pivot: high -= 1
        if low<high:
            A[low], A[high] = A[high], A[low]
    A[high], A[left] = A[left], A[high]
    return high