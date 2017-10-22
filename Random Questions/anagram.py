'''
You have two strings s and t,
check if t's anagram is present in s
'''
from collections import Counter
def question(s,t):
    s=s.lower() #Convert both strings to their lower cases
    t=t.lower()
    #create counter for pattern
    ct=Counter(t)
    #a list to find the indexes of the match in text
    l=[]
    for i in range(len(s)-len(t)+1): #O(n-m)
        #find substring
        sub_s=s[i:i+len(t)]
        cs=Counter(sub_s) #O(m)
        #match this substring counter with the pattern
        if cs==ct: #O(m)
            l.append(i)
    return l
s=input("Enter the main string: ")
t=input("Enter the string to check: ")
print(question(s,t))
