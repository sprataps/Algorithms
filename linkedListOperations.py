class Node:
    def __init__(self,data=None,next=None):
        self.data=data
        self.next=next

class Linkedlist:
    def __init__(self):
        self.head=None

    def addLast(self,data=None,next=None):
        node=Node(data,next)
        start=self.head
        if self.head==None:
            self.head=Node(data)
        else:
            while(start.next!=None):
                start=start.next
            start.next=node

    def addFirst(self,data=None,next=None):
        node=Node(data)
        if self.head==None:
            self.head=node
        else:
            node.next=self.head
            self.head=node

    def printList(self):
        if self.head==None:
            print ("Empty List")
        else:
            start=self.head
            while(start!=None):
                print(start.data,end=" ")
                start=start.next
            print("\n")

    #delete middle element of a linked List
    def deleteMiddleElement(self):
        slow=self.head
        fast=self.head
        prev=Node(None,self.head)
        while(fast.next!=None and fast.next.next!=None):
            fast=fast.next.next
            slow=slow.next
            prev=prev.next
        print("Middle of the given linked list: ",slow.data)
        prev.next=slow.next

    #remove duplicates from  linked list
    def removeDuplicates(self):
        start=self.head
        prev=Node(None,start)
        while(start!=None):
            if prev.data==start.data:
                prev.next=start.next
                start=start.next.next
                prev=prev.next
            else:
                start=start.next
                prev=prev.next

    #detect loop in linked List
    def detectLoop(self):
        slow=self.head
        fast=self.head
        while ( slow!=None and fast!=None):
            if slow is fast:
                return True
            slow=slow.next
            fast=fast.next.next
        return(False)

    def length(self):
        if self.head==None:
            print("Empty List")
            return 0
        else:
            l=1
            start=self.head
            while(start!=None):
                start=start.next
                l+=1
            return l

    def removeLoop(self):
        slow=self.head
        fast=self.head
        loopStart=None
        while ( slow!=None and fast!=None):
            if slow is fast:
                loopStart=slow
                break
            slow=slow.next
            fast=fast.next.next
        i=1
        while(loopStart.next!=slow):
            loopStart=loopStart.next
            i+=1
        len=self.length()
        start=self.head()
        j=1
        while(j<len-i):
            start=start.next
        while(j<len):
            start=start.next
        start.next=None

    def removeNth(self,n):
        len=self.length()
        i=1
        start=self.head
        prev=Node(None,start)
        while (i<n):
            start=start.next
            prev=prev.next
            i+=1
        prev.next=start.next

    def reverseLinkedList(self):
        prev=self.head
        present=self.head.next
        past=Node()
        while(present!=None):
            temp=present.next
            present.next=prev
            prev.next=past
            past=present.next
            prev=present
            present=temp
            self.head=prev

    def palindrome(self):
        slow=self.head
        fast=self.head
        while(fast.next != None and fast.next.next!=None):
            slow=slow.next
            fast=fast.next.next
        ll=Linkedlist()
        while(slow!=None):
            ll.addFirst(slow.data)
            slow=slow.next
        firstList=self.head
        secondList=ll.head
        while(firstList!=None and secondList!=None):
            if firstList.data!=secondList.data:
                return False
            firstList=firstList.next
            secondList=secondList.next
        return True


'''
print("Enter the elements of the linkedlist separated by space:")
l=[int(x) for x in input().split()]
print(l)
ll=Linkedlist()
i=0
for i in range(len(l)):
    ll.addLast(l[i])
ll.printList()
ll.deleteMiddleElement()
ll.printList()

l=[int(x) for x in input("Enter linked list with duplicates").split()]
ll1=Linkedlist()
for i in range(len(l)):
    ll1.addFirst(l[i])
ll1.printList()
ll1.removeDuplicates()
ll1.printList()

l=[int(x) for x in input("Enter linked list with duplicates").split()]
ll1=Linkedlist()
for i in range(len(l)):
    ll1.addLast(l[i])
ll1.printList()
print(ll1.detectLoop())

l=[int(x) for x in input().split()]
ll=Linkedlist()
for i in range(len(l)):
    ll.addLast(l[i])
ll.printList()
ll.removeNth(3)
ll.printList()

l=[int(x) for x in input().split()]
ll=Linkedlist()
for i in range(len(l)):
    ll.addLast(l[i])
ll.printList()
ll.reverseLinkedList()
ll.printList()
'''

l=[int(x) for x in input().split()]
ll=Linkedlist()
for i in range(len(l)):
    ll.addLast(l[i])
ll.printList()
print(ll.palindrome())
