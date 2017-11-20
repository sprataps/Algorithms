'''
Rabin Karp associates the pattern and the subsequent pettern length words in the string to a hash value.
This hash value for each substring andthe pattern is compared.
A complete match of the pattern and the substring is done if their hash values match.
This algorithm is used for find occurences of pattern in a given string.
'''

class RabinKarp:
    def __init__(self,text,length):
        self.text=text
        self.hash=0
        self.window_start=0
        self.window_end=length
        self.pattern_length=length
        for i in range(0,length):
            self.hash += ord(self.text[i])*(256**(length-i-1))

    def moveWindow(self):
        self.hash -= ord(self.text[self.window_start])*(256**(self.pattern_length-1))
        self.hash *= 256 #shift every character by one position to the left
        self.hash += ord(self.text[self.window_end])
        print(self.text[self.window_end])
        self.window_start+=1
        self.window_end+=1


def rabinKarp(s,p):
    object_s=RabinKarp(s,len(p))
    object_p=RabinKarp(p,len(p))
    print("Object s String: ",object_s.text)
    l=[]
    if len(p)>len(s):
        print("Pattern cannot be larger than the string")
        return
    for i in range(0,len(s)-len(p)+1):
        if object_s.hash==object_p.hash:
            if s[i:i+len(p)]==p:
                l.append(i)
        object_s.moveWindow()
    print("\nPositions where the pattern occurs in the string: ",l)

pattern=input("\nEnter the pattern to check: ")
string=input("\nEnter the string to check the pattern in: ")
rabinKarp(string,pattern)
