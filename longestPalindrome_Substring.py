'''
Given a string a, find the longest palindromic substring contained in a.
Idea: Pick an index, start from it in either directions till we get a match.
Find the longest matchedstring for both odd and even positions.
O(n^2)
'''

def longestPalindrome(s):
    maxLength=1

    start=0
    l=len(s)
    low=0
    high=0

    for i in range(1,l):
        #create even sized strings in s
        low=i-1
        high=i
        while (low>=0) and (high<l) and s[low]==s[high]:
            #check for palindrome
            if high-low+1>maxLength:
                start=low
                maxLength=high-low+1
            low-=1
            high+=1

        #create odd sized strings in s
        low=i-1
        high=i+1
        while( low>=0) and (high<l) and s[low]==s[high]:
            #check for palindrome
            if high-low+1>maxLength:
                start=low
                maxLength=high-low+1
            low-=1
            high+=1
    print(s[start:maxLength+start])
    return maxLength
s=input("Enter the string to search the palindrome in: ")
print(longestPalindrome(s))

'''
MANACHERS Algorithm
Idea:
