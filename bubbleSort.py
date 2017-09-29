def bubbleSort(l):
    for i in range(len(l)):
        m=i
        for j in range(len(l)):
            if l[m]<l[j]:
                l[m],l[j]=l[j],l[m]
    print (l)

arr=[int(x)for x in input().split()]
bubbleSort(arr)
