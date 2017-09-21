#Implementing a stack using a linked list
class Node:
    def __init__(self,value=None):
        self.value=value
        self.next=None
    def __str__(self):
        print (self.value)

class LinkedList:
    def __init__(self):
        self.head=Node()

    def insertFirst(self,val):
        temp=Node(val)
        if not self.head:
            self.head=temp
            return
        else:
            temp1=self.head
            self.head=temp
            self.head.next=temp1
        return

    def DeleteFirst(self):
        if not self.head:
            return None
        temp=self.head
        self.head=self.head.next
        return temp.value

    def printList(self):
        if not self.head:
            print("Empty")
        cur=self.head
        while(cur.next):
            print(cur.value)
            cur=cur.next

class Stack:
    def __init__(self,top=None):
        temp=LinkedList()
        self.top=temp

    def push(self,val):
        self.top.insertFirst(val)

    def pop(self):
        val=self.top.DeleteFirst()
        print(val)

    def printStack(self):
        self.top.printList()

s1=Stack()
s1.push(1)
s1.push(2)
s1.push(3)
s1.printStack()
s1.pop()
s1.printStack()
