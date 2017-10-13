'''
find if the string exists as a substring in
another string.
'''

s=input("Enter the main string: ")
t=input("Enter the substring: ")
substringSearch1(s,t)


#naive approach O(n^2)
def substringSearch1(s,t):
    print("Found at: ",end=" ")
    l=len(t)
    for i in range(0,len(s)):
        if s[i]==t[0]:
            if t==s[i:i+l]:
                print(i+1,end=" ")

#Rabin Karp Algorithm 
def substringSearch2(s,t):
