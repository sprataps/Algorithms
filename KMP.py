'''
Knuth Morris Pratt Algorithm
O(n) time complexity
IDea:
    If there is a mismatch in the pattern and text, we need not start the match from the beginning of the pattern.
    A mismatch suggests that a match happened previously between a prefix of the pattern till this mismatch position and
    a part of the text. This part of the text now is similar to a proper suffix of the pattern. If we know how many prefix of the
    pattern match with the suffix of the pattern until this position, we can shift this length so that we don't need to match
    whole of the pattern with the window in the text again.
'''

'''
To calculate the length of the longest prefix that matches the longest suffix.
For each index, store the length of the longest prefix-suffix match.
If they don't match and the length of the longest match is 0, then store 0 for that index
else iterate back on the matching length till we find the longest length that matches.
'''

def calculateArray(pat,table):
    matchLen=0 #the length of the longest prefix that matches the suffic till any index
    index=1 #to match from the index 1 to the entire length of the pattern

    for index in range(1,len(pat)):
        if pat[index]==pat[matchLen]:
            matchLen+=1
            table[index]=matchLen
            index+=1
        else:
            if len!=0:
                len=table[len-1]
            else:
                table[index]=0
                index+=1

def knuthMorrisPratt(text,pat):
    table=[0]*lem(pat)
    calculateArray(pat,table)
    i=0 #index that runs over the text
    j=0#index to run over pattern
    for i in range(0,len(text)):
        if pat[j] == text[i]:
            i+=1
            j+=1
        if j==len(pat):#when entire pattern matches with some substring of text
            print("Found at: ",str(i-j))
            j=table[j-1] #shift the characters to match using the table

        elif i< len(text) and pat[j]!=text[i]:
            #if the current value doesn't match then jump the characters to match as previous ones match
            if j!=0:
                j=table[j-1]
            else:
                i+=1

text=input("Enter the text: ")
pat=input("Enter the pattern to be searched in the string: ")
knuthMorrisPratt(text,pat)
