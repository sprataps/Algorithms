'''
find if the string exists as a substring in
another string.
'''

#naive approach O(n^2)
def substringSearch1(s,t):
    print("Found at: ",end=" ")
    l=len(t)
    for i in range(0,len(s)): #O(n)
        if s[i]==t[0]:
            if t==s[i:i+l]: #O(n) worst (Can we reduce this?)
                print(i+1,end=" ")

#Rabin Karp Algorithm
def substringSearch2(s,t):
    h=11 #base
    sum_t=0
    for i in range(len(t)):
        print(ord(t[i]),"  ",len(t)-i-1)
        sum_t+=ord(t[i])*(h**(len(t)-i-1))
    print("The value for the substring is: {}".format(sum_t))
    sub_string=s[0:len(t)]
    sum_s=0
    for i in range(0,len(t)):
        sum_s+=ord(s[i])*(h**(len(t)-i-1))
    print("The value of hash at beginning of string is: ",sum_s)
    l=[]
    if sum_s==sum_t:
        l.append([0,len(t)])
    for i in range(1,len(s)-len(t)+1): O(n)
        sum_s-=(h**(len(t)-1))*ord(s[i-1])
        sum_s*=h
        sum_s+= ord(s[i+len(t)-1])
        print("Hash code now at ",i," is: ",sum_s)
        if sum_s==sum_t: 
            l.append([i,(i+len(t))])
    print("Found values at the places: ",l)

s=input("Enter the main string: ")
t=input("Enter the substring: ")
substringSearch2(s,t)
