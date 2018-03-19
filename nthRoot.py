import math


def root(x,n):
  low=0
  high=x
  mid=low+ (high-low)/2.0
  while(low<high and mid ** n >=.001):
    mid= low+ (high-low)/2.0
    if mid ** n > x:
      high=mid
    elif mid ** n <x:
      low=mid + .001
    else:
      return mid
  return mid

print(root(3,2))


def mySqrt( x):
    """
    :type x: int
    :rtype: int
    """
    if x==0:
        return 0
    left=1
    right=x
    while(left<=right):
        mid=(left+right)/2
        if mid<=(x/mid):
            print("Mid: ",mid)
            left=mid+1
            ans=mid
        else:
            right=mid-1
            print("Right: ",right)
    return ans

x=int(input("Enter number"))
n=int(input("enter the root"))
#print(nthRoot(x,n))

print(mySqrt(x))
