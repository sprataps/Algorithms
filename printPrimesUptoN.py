import math
def primes(n):
    l=[1]*(n+1)
    l[0]=0
    l[1]=0
    for i in range(2,int(math.sqrt(n))+1):
        if l[i]==1:
            for j in range(i*2,n+1,i):
                l[j]=0
    for k in range(0,len(l)):
        if l[k]==1:
            print (k,end=" ")

n=int(input())
(primes(n))
