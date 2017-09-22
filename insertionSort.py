def insertionSort(arr):
    for i in range(1,len(arr)):
        temp=arr[i]
        j=i-1
        while temp<arr[j] and j>=0:
            arr[j+1]=arr[j]
            j-=1
        arr[j+1]=temp 
        print("Incrementing i: {}".format(arr))


arr=[int(x)for x in input().split()]
insertionSort(arr)
print(arr)
