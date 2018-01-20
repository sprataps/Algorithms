'''
Program to print all possible permutaions of a given string.
The left list is used to hold all the unused charaters in the permutations.
The used list is used to hold all the used cahracters in the permutations.
'''

def permutations(string):
    def sub_routine(used,left):
        combos=[]
        for i in range(0,len(left)):
            ch=left.pop(i)
            used.append(ch)

            combos.append(''.join(used))
            combos=combos+ sub_routine(used,left)

            used.pop(-1)

            left[i:0]=[ch]

        return combos

    return sub_routine([], list(string))


def permutations1(string):
    stack=list(string)
    results= [stack.pop()] #first remove the first character of the string
    while (len(stack)!=0):
        c=stack.pop() #pop the first character of the string
        new_results= []
        for w in results:
            for i in range(len(w)+1):
                new_results.append(w[:i]+ c + w[i:])
        results= new_results
    return results


def main():
    s=input("Enter the string to print the permutations of: ")
    print (permutations1(s))

if __name__=="__main__":
    main()
