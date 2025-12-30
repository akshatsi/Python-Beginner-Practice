def selection_sort(a):
    n = len(a)
    for i in range (0,n-1 ):
        b = a[i]
        c = i
        for j in range(i ,n):
            if a[j]<b:
                b = a[j]
                c = j   
            else:
                continue     
        x = a[i]            
        a[i] = a[c]
        a[c] = x
    return a

a = [101,89,93,32,1,45,98, 1005, 23]
b = selection_sort(a)
print("selection sort:" , b )

def bubble_sort(a):
    n = len(a)
    for i in range(0, n-1):
        did_swap = 0
        for j in range(0, n-i-1):
            if a[j] > a[j+1]:
                c = a[j]
                a[j] = a[j+1]
                a[j+1] = c
                did_swap = 1
            else:
                continue
        if did_swap == 1:
            break
    return a
print("bubble sort:",bubble_sort(a)) 

def insertion_sort(a):
    n = len(a)
    for i in range(0, n):
        j = i
        while j>0 and a[j-1]> a[j]:
            c = a[j]
            a[j] = a[j-1]
            a[j-1] = c
            j = j-1
    return a

print("insertion sort:", insertion_sort(a))

x = a[0]
y = a[-1]
def merge( arr, low, mid, high):
        temp = []
        left, right = low, mid + 1

        # Merge both sorted halves
        while left <= mid and right <= high:
            if arr[left] <= arr[right]:
                temp.append(arr[left])
                left += 1
            else:
                temp.append(arr[right])
                right += 1

        # Add remaining left elements
        while left <= mid:
            temp.append(arr[left])
            left += 1

        # Add remaining right elements
        while right <= high:
            temp.append(arr[right])
            right += 1

        # Copy sorted temp into original array
        for i in range(low, high + 1):
            arr[i] = temp[i - low]

    # Recursive merge sort
def mergeSort( arr, low, high):
        if low >= high:
            return
        mid = (low + high) // 2
        mergeSort(arr, low, mid)
        mergeSort(arr, mid + 1, high)
        merge(arr, low, mid, high)
        return arr

print(mergeSort(a, 0,len(a)-1 ))