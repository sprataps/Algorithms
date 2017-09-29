def selectionSort(l):
    for i in range(len(l)):
        m=i
        for j in range(i,len(l)):
            if l[i]>l[j]:
                m=j
        l[i],l[m]=l[m],l[i]

    print(l)

x=[int(x) for x in input().split()]
selectionSort(x)
