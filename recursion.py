'''
This is a startup kit for recursion.
Contains basic functions for which there is no recursive formula given.

Helps to get started before taking up problems on backtracking.
'''

#Problem1
'''
Print digits of a number in reverse order
'''
from math import log10
def printReverseDigits(number):
    if number<10:
        return number
    return ((number%10)*10 ** int(log10(number//10) +1) +printReverseDigits(number//10))

#its iterative solution
def iterativeReverseDigits(number):
    ret=0
    while(number>0):
        temp=number%10
        ret=ret*10+temp
        number=number//10
    return ret

print(iterativeReverseDigits(1239))

#Problem2
'''
Check for palindrome
'''
print("PALINDROME")
def recursivePalindrome(s):
    if len(s)==0:
        return True
    return s[0]==s[-1] and recursivePalindrome(s[1:-1])
    return False

print(recursivePalindrome("paap"))

#iterative palindrome
def iterativePalindrome(s):
    for i in range(len(s)//2):
        if s[i]!=s[len(s)-i-1]:
            return False
    return True

print(iterativePalindrome("NOPALindrome"))


'''
Binary Search
'''

print("BINARY SEARCH")
def recursiveBinarySearch(arr,start,end,target):
    mid=(start+end)//2
    if start>end:
        return "Not Found"
    if target==arr[mid]:
        return mid
    else:
        if target<arr[mid]:
            return recursiveBinarySearch(arr,start,mid-1,target)
        else:
            return recursiveBinarySearch(arr,mid+1,end,target)

arr=[int(c) for c in input().split()]
start=0
end=len(arr)-1
target=int(input("Enter the number to search"))
print(recursiveBinarySearch([1,2,3,4,5],0,4,4))
