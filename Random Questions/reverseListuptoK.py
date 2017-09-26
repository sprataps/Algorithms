'''
given an array of numbers,
reverse the array from starting to the kth number
'''

def reverse(l,k):
    n=len(l)-1
    for i in range(0,int(k/2)):
        temp=l[n-k-i]
        l[n-k-i]=l[i]
        l[i]=temp
    print (l)

l=[ int (x) for x in input().split()]
k=int(input("Enter number: "))
reverse(l,k)
