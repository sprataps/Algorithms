def binarySearch(arr,val):
    mid=len(arr)/2
    left=0
    right=len(arr)-1
    arr.sort()
    while(left<=right):
        mid=int(left+(right-left)/2)
        if arr[mid]==val:
            return mid
        elif arr[mid]<val:
            left=mid+1
        else:
            right=mid-1
    return "Not Found"

arr=[int(x) for x in input("Enter array: ").split()]
val=int(input("Enter value: "))
print(binarySearch(arr,val))
