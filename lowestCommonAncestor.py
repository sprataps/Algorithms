'''
Find the least common ancestor between two nodes on a binary search tree. The least common ancestor is the farthest node from the root that is an ancestor of both nodes. For example, the root is a common ancestor of all nodes on the tree, but if both nodes are descendents of the root's left child, then that left child might be the lowest common ancestor. You can assume that both nodes are in the tree, and the tree itself adheres to all BST properties. The function definition should look like question4(T, r, n1, n2), where T is the tree represented as a matrix, where the index of the list is equal to the integer stored in that node and a 1 represents a child node, r is a non-negative integer representing the root, and n1 and n2 are non-negative integers representing the two nodes in no particular order. For example, one test case might be

question4([[0, 1, 0, 0, 0],
           [0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0],
           [1, 0, 0, 0, 1],
           [0, 0, 0, 0, 0]],
          3,
          1,
          4)
and the answer would be 3.
'''
def lowestCommonAncestor(T,r,n1,n2):
    if not T:
        return
    elif len(T)<max(r,n1,n2):
        print("Inputs mismatch")

    #find all parents of n1 and n2
    l=0
    n1Parent=[]
    if n1==r:
        return n1
    else:
        while(n1!=r):
            while(l<len(T)):
                if T[l][n1]==1:
                    print("Parent of ",n1," is ",l)
                    n1Parent.append(l)
                    break
                l+=1
            n1=l
            l=0
    l=0
    n2Parent=[]
    if n2==r:
        return n2
    else:
        while(n2!=r):
            while(l<len(T)):
                if T[l][n2]==1:
                    print("Parent of ",n2," is ",l)
                    n2Parent.append(l)
                    break
                l+=1
            n2=l
            l=0
    for i in n1Parent:
        for j in n2Parent:
            if i==j:
                return i
    return None

print(lowestCommonAncestor([[0,1,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[1,0,0,0,1],[0,0,0,0,0]],3,1,4))
