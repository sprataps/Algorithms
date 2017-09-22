def mergeSort(arr):
    if len(arr)==0 or len(arr)==1:
        return arr
    else:
        q=int((len(arr))/2)
        a=mergeSort(arr[:q])
        b=mergeSort(arr[q:])
        return merge(a,b)


def merge(a,b):
    c=[]
    i=0
    j=0
    while i<len(a) and j<len(b):
        if a[i]<b[j]:
            c.append(a[i])
            i+=1
        else:
            c.append(b[j])
            j+=1

    if i==len(a):
        c+=b[j:]
    elif j==len(b):
        c+=a[i:]
    return c

arr=[int(x) for x in input().split()]
arr=mergeSort(arr)
print(arr)
