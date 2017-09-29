def bubbleSort(l):
    n=len(l)
    for i in range(len(l)):
        m=i
        swappped=False
        for j in range(l0,n-i-1)):
            if l[m]<l[j]:
                l[m],l[j]=l[j],l[m]
            swapped=True
        if swapped==False:
            break
    print (l)

arr=[int(x)for x in input().split()]
bubbleSort(arr)

'''
Best Case: No swap occurs in inner loop.
Worst and Average= O(n^2)
Stable
In-place
'''
