'''
problem 1:
Largest sum contiguous subarray
Popularly known as the Kadane's Algorithm
'''

def problem1(arr):
    curSum=arr[0]
    maxSum=arr[0]
    tempSum=-99999
    for i in range(1,len(arr)):
        curSum=max(arr[i],curSum+arr[i])
        maxSum=max(maxSum,curSum) #calculates the maximum sum subarray
    return maxSum

#arr=[int(x) for x in input("Enter the array: ").split()]
#print(problem1(arr))

'''
Problem 2:
Find the maximum sum of a subarray of size k
'''
def problem2(arr,k):
    maxSum=0
    curSum=0
    tempArr=arr[0:k]
    #Get the sum of the first k elements in the array
    for j in range(k): #O(k)
        curSum+=arr[j]
    if curSum>0:
        maxSum=curSum
    for i in range(k,len(arr)):
        curSum-=arr[i-k]
        curSum+=arr[i]
        if curSum>maxSum:
            maxSum=curSum

    return maxSum


#arr=[int(x) for x in input("Enter the array: ").split()]
#k=int(input("Enter the maximum length: "))
#print(problem2(arr,k))


'''
Problem 3:
Largest sum subarray with atleast k numbers
'''

def problem3(arr,k):
    maxSum=[0] * (len(arr)+1)
    curSum=0
    curLength=0
    maxLength=0
    #calculate maximum sum till each index, either this includes this number or some more numbers including the number at this index
    for i in range(len(arr)):
        curSum=max(arr[i],curSum+arr[i])
        maxSum[i]=curSum

    curSum=sum(arr[0:k])
    res= curSum
    for j in range(k,len(arr)):
        curSum+=arr[j]
        curSum-=arr[j-k]
        res=max(res,curSum)
        res=max(res,curSum+maxSum[j-k])
    print(res)

#arr=[int(x) for x in input("Enter the array: ").split()]
#k=int(input("Enter the minimum length: "))
#(problem3(arr,k))

'''
Problem 4:
Largest sum subarray with atmost k numbers
'''


def problem4(arr,k):
    curSum=arr[0]
    maxSum=arr[0]
    tempSum=-99999
    l=1
    for i in range(1,len(arr)):
        if arr[i]>curSum+arr[i]:
            l=1
            curSum=arr[i]
        else:
            l+=1
            curSum=curSum+arr[i]
        if l<=k:
            maxSum=max(maxSum,curSum)
            maxLength=l
    print("Length of maximum length subarrya: ",maxLength)
    return maxSum

#arr=[int(x) for x in input("Enter the array: ").split()]
#k=int(input("Enter the maximum length of the array: "))
#print(problem4(arr,k))

'''
Problem5:
Find subarray of given sum
this problem can be distilled down to a two sum problem.
Use a hashtable to store curSum for each index, if curSum-desiredSum exists in the table,
this means that curSum-(curSum-desiredSum) exists in the array.
'''
def problem5(arr, sum):
    n=len(arr)
    curSum = arr[0]
    start = 0
    hashTable={0:0,arr[0]:1}
    i = 1
    while i <= n:
        if curSum-sum in hashTable:
            return [hashTable[curSum-sum],i-1]
        else:
            hashTable[curSum]=i
        curSum+=arr[i]
        i+=1
    print ("No subarray found")
    return 0

#arr=[int(x) for x in input("Enter the array: ").split()]
#k=int(input("Enter the desired sum: "))
#print(problem5(arr,k))

'''
Problem 6
Longest Subarray having sum of elements atmost 'k'
'''

def problem6(arr,k):
    sumMax=arr[0]
    lengthMax=1
    maxLength=0
    for i in range(1,len(arr)):
        if sumMax+arr[i]<k:
            lengthMax+=1
            sumMax+=arr[i]
        elif sumMax+arr[i]>k:
            if lengthMax>maxLength:
                maxLength=lengthMax
            lengthMax=0
            sumMax=arr[i]
        else:
            if lengthMax>maxLength:
                maxLength=lengthMax
            lengthMax=0
    if maxLength!=0:
        return maxLength
    else:
        return len(arr)

#arr=[int(x) for x in input("Enter the array: ").split()]
#k=int(input("Enter the maximum sum: "))
#print(problem6(arr,k))


'''
Problem 7:
Find smallest subarray which exceeds given sum
For positive numbers only
'''
def problem7(arr,k):
    sumMin=arr[0]
    lengthMin=1
    minLength=len(arr)
    for i in range(1,len(arr)):
        if sumMin+arr[i]<=k:
            lengthMin+=1
            sumMin+=arr[i]
        else:
            if lengthMin<=minLength:
                minLength=lengthMin
            lengthMin=1
            sumMin=arr[i]
    return minLength

arr=[int(x) for x in input("Enter the array: ").split()]
k=int(input("Enter the maximum sum: "))
print(problem7(arr,k))
