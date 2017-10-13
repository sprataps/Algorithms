'''
pass two string s and t
return True if s contains a substring which is anagram of t
'''

def question1(s,t):
    d={}
    l=len(t)
    s=s.lower()
    t=t.lower()
    t="".join(sorted(t))
    print("Sorted substring: "+t)
    for i in range(0,len(s)):
        d[s[i]]=i
    for i in range(l-1,len(s)-l): #O(n)
        if s[i] in t:
            temp="".join(sorted(s[i:i+l])) #O(nlogn)
            print(temp)
            if temp==t:
                return True
    return False






s=input("Enter the main string: ")
t=input("Enter the string to check in main string: ")
print(question1(s,t))
