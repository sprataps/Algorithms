'''
Quicksort
- In place sorting algorithm.
- Point lies in selecting the pivot:
    - Choose the last value in arr (implemented here)
    - Choose the first value in arr
    - Choose median
    - Choose randomly

Worst Run time:
    Time complexity : O(n^2)
    T(n) = T(n-1) + constant

Best Case:
    Time Complexity: O(nlogn)

Average Case:
    Time Complexity: O(nlogn)

'''
#Recursive QuickSort

def partition(arr,low,high):
    i=low-1
    pivot=arr[high]
    for j in range(low,high):
        if arr[j]<=pivot:
            i+=1
            arr[i],arr[j]=arr[j],arr[i]
    arr[i+1],arr[high]=arr[high],arr[i+1]
    return i+1

def quickSortRecursive(arr,low,high):
    if low<high:
        index=partition(arr,low,high)
        quickSortRecursive(arr,low,index-1)
        quickSortRecursive(arr,index+1,high)

arr=[int(x) for x in (input().split())]
quickSortRecursive(arr,0,len(arr)-1)
print("Sorted: ",arr)
