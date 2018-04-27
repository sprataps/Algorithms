def findValue(arr,val):
    high=1
    low=0
    while(val>arr[high]):
        low=high
        high=2*high
    print(low,high)
    index=findIndex(arr[low:high+1],val)
    print("Found at: ",str(index+low))

def findIndex(arr,val):
    low=0
    high=len(arr)
    while(low<high):
        mid=low+(high-low)//2
        if val==arr[mid]:
            return mid
        elif val<arr[mid]:
            high=mid-1
        else:
            low=mid
    return low

arr=[int(x) for x in input("Enter array: ").split()]
val=int(input("Enter value to search:"))
print(findIndex(arr,val))
