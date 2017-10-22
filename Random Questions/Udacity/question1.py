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
    for i in range(0,len(s)): #O(n)
        if s[i] in t:
            temp="".join(sorted(s[i:i+l])) #O(nlogn)
            print(temp)
            if temp==t:
                return True
    return False

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
t=input("Enter the string to check in main string: ")
print(question1(s,t))
