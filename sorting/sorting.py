# insertion sort algorithm  1,7,4,8,3,0 siralamak için algorıtma yazacaksan
import timeit

def insertion_sort_while(A):
    for i in range(1, len(A)):
        j = i-1
        while A[j] > A[j+1] and j >= 0:
            A[j], A[j+1] = A[j+1], A[j]
            j -=1


def insertion_sort(A):
    for i in range(1, len(A)):
        for j in range(i-1, 0, -1):
            if A[j] > A[j+1]:
                A[j], A[j+1] = A[j+1], A[j]
            else:
                break

def fast_insertion_sort(A):
    for i in range(1, len(A)):
        curNum= A[i]
        for j in range(i-1,0,-1):
            if A[j] > curNum:
                A[j+1] = A[j]
            else:
                A[j+1] = curNum
                break

# Eger iki kat hizlandirmak istiyorsak kodu asagidaki methodu kullaniyoruz


start = timeit.default_timer()
elma = [ 1,3,6,2,84,2,5]
print(elma)
insertion_sort(elma)
print ( elma )
stop = timeit.default_timer()
print('Time: ', stop - start)
print("fast_insertion")


# Hizli çalıştırmak istiyorsan
start = timeit.default_timer()
elma = [ 1,3,6,2,84,2,5]
print(elma)
fast_insertion_sort(elma)
print ( elma )
stop = timeit.default_timer()
print('Time: ', stop - start)

# Selection Sort
# Neting loop kullandigi icin cok kotu

def selection_sort(A):
    for i in range(0, len(A)-1):
        minIndex = i
        for j in range(i+1, len(A)):
            if A[j] < A[minIndex]:
                minIndex = j
        if minIndex != i:
            A[i], A[minIndex] = A[minIndex], A[i]

print("selection sort")
elma = [ 1,3,6,2,84,2,5]
print(elma)
selection_sort(elma)
print(elma)

# Buble sort function
# Buyuk oldugunda merge sort kullanmalisin
# It is relatively slow

def bubleSort(myList):
    for i in range(0, len(myList)-1):
        for j in range(0, len(myList)-1-i):
            if myList[j]> myList[j+1]:
                myList[j], myList[j+1] = myList[j+1], myList[j]
    return myList
print("buble sort")
theList = ['b','d','f','a','c','e']
print(theList)
print(bubleSort((theList)))

# Merge Sort, divide-and-conquer algorithm #very effecient for large datasets
# Merge sort listeleri ikiye boluyor sonra ilk bastakileri karsilartiriyor

def merge_sort(A):
    merge_sort_2(A,0,len(A)-1)

def merge_sort2(A, first,last):
    if first < last:
        middle = (first + last)// 2
        merge_sort2(A,first,middle)
        merge_sort2(A,middle+1,last)
        merge(A,first,middle,last)

def merge(A,first,middle,last):
    L= A[first:middle]
    R = A[middle:last+1]
    L.append(999999999)
    R.append(999999999)
    i=j=0
    for k in range(first,last+1):
        if L[i] <= R[j]:
            A[k] = L[i]
            i +=1
        else:
            A[k] = R[j]
            j+=1

# quick sort nasil olutyor

def quick_sort(A):
    quick_sort2(A,0,len(A)-1)

def get_pivot(A,low ,hi):
    mid = (hi + low) // 2
    pivot = hi
    if A[low] < A[mid]:
        if A[mid]<A[hi]:
            pivot = mid
    elif A[low] < A[hi]:
        pivot = low
    return pivot


def partition(A,low,hi):
    pivotIndex = get_pivot(A,low,hi)
    pivotValue = A[pivotIndex]
    A[pivotIndex],A[low] = A[low], A[pivotIndex]
    border = low

    for i in range(low, hi+1):
        if A[i] < pivotValue:
            border += 1
            A[i], A[border] = A[border], A[i]
    A[low], A[border] = A[border], A[low]

    return border

def quick_sort2(A,low,hi):
    if low<hi:
        p = partition(A,low,hi)
        quick_sort2(A,low,p-1)
        quick_sort2(A,p+1,hi)




def quick_sort2_upgraded(A,low,hi):
    threshold = 10
    if hi-low < threshold and low<hi:
        quick_selection(A,low,hi)
        # bunu kendin ayarlayacaksin
    elif low<hi:
        p = partition(A,low,hi)
        quick_sort2(A,low,p-1)
        quick_sort2(A,p+1,hi)

print("quick sort")
elma = [ 1,3,6,2,84,2,5,10,43,1,43,13,53,54]
print(elma)
print(quick_sort((elma)))



