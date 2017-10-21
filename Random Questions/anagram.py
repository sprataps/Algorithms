'''
You have two strings s and t,
check if t's anagram is present in s
'''
from collections import Counter
def question(s,t):
    s=s.lower()
    t=t.lower()
    ct=Counter(t)
    l=[]
    for i in range(len(s)-len(t)+1): #O(n-m)
        sub_s=s[i:i+len(t)]
        cs=Counter(sub_s) #O(m)
        if cs==ct: #O(m)
            l.append(i)
    return l
s=input("Enter the main string: ")
t=input("Enter the string to check: ")
print(question(s,t))
