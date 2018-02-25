'''
Find the element in a singly linked list that's m elements from the end.
For example, if a linked list has 5 elements, the 3rd element from the end is the 3rd element.
The function definition should look like question5(ll, m), where ll is the first node of a linked list and m is the "mth number from the end".
You should copy/paste the Node class below to use as a representation of a node in the linked list. Return the value of the node at that position.
'''

def mElement(l1,m):
    if not  l1:
        return None
    i=0
    j=0
    walker=Node(None)
    main=Node(None)
    walker.next=l1
    main.next=l1
    #iterate walker to next for m times
    while(i<m):
        walker=walker.next
    #iterae walker till last, iterate main alingwith it, when walker reaches end, main has reached =length-m+1
    while(walker):
        walker=walker.next
        main=main.next
    return main.val
