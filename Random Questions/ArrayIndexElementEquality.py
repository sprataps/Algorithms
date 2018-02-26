'''
Given a sorted array arr of distinct integers, write a function
 indexEqualsValueSearch that returns the lowest index i for which
 arr[i] == i. Return -1 if there is no such index. Analyze the time
  and space complexities of your solution and explain its correctness.
'''







def index_equals_value_search(arr):
  start=0
  end=len(arr)-1
  while(start<=end):
    i=int((start+end)/2)
    if arr[i]-i<0:
      start=i+1
    elif ((arr[i]-i==0) and ((i==0) or (arr[i-1]-(i-1))<0)):
      return i
    else:
      end=i-1
  return -1
