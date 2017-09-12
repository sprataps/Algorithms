import copy
class Node:
    def __init__(self,data=None,next=None):
        self.data=data
        self.next=next

    def __str__(self):
        return str(self.data)
    def printBackwards(self):
        if self.next!=None:
            tail=self.next
            tail.printBackwards()
        print (self.data)

class LinkedList:
    def __init__(self):
        self.head=None

    def add(self,data):
        node=Node(data)
        if self.head==None:
            self.head=node
        else:
            node.next=self.head
            self.head=node

    def printList(self):
        node=self.head
        while node!=None:
            print(node.data)
            node=node.next

    def addLast(self,data):
        node=self.head
        nodeNew=Node(data)
        if self.head==None:
            self.head=nodeNew
        else:
            while node.next!=None:
                node=node.next
            node.next=nodeNew
            nodeNew.next=None

    def printBackwards(self):
        node=self.head
        if node!=None:
            node.next.printBackwards()
        else:
            print (node.data)

    def reverseList(self):
        node=self.head
        prev=None
        while(node!=None):
            nextNode=node.next
            node.next=prev
            prev=node
            node=nextNode
        self.head=prev

    def addOne(self):
        self.reverseList()
        node=self.head
        carry=1
        prev=Node()
        while node!=None:
            node.data+=carry
            if node.data>9:
                node.data=0
                carry=1
            else:
                carry=0
            prev=node
            node=node.next
        if prev.data>9:
            temp=Node(1)
            prev.data=0
            prev.next=temp
        self.reverseList()

list1=LinkedList()
list1.addLast(1)
list1.addLast(2)
list1.addLast(9)
list1.addOne()
list1.printList()
