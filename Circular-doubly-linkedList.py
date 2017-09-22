class Node:
    def __init__(self,val=None):
        self.val=val
        self.next=None
        self.prev=None

    def __str__(self):
        return str(self.val)

class DoublyLinkedList:
    def __init__(self):
        self.firstNode=None
        self.lastNode=None
        self.size=0

    def insertAtHead(self,val):
        firstNode=Node(val)
        if not self.firstNode:
            self.firstNode=firstNode
            self.lastNode=firstNode
            self.firstNode.prev=self.lastNode
            self.lastNode.next=self.firstNode
        else:
            next=self.firstNode
            prev=self.lastNode
            firstNode.next=next
            firstNode.prev=prev

            next.prev=firstNode
            prev.next=firstNode
            self.firstNode=firstNode

    def insertAtTail(self,val):
        lastNode=Node(val)

        self.lastNode.next=lastNode
        self.firstNode.prev=lastNode

        lastNode.next=self.firstNode
        lastNode.prev=self.lastNode
        self.lastNode=lastNode

    def deleteAtHead(self):
        if not self.firstNode:
            return None
        else:
            node=self.firstNode
            next=self.firstNode.next
            self.firstNode=next
            self.lastNode.next=next
            next.previous=self.lastNode
            return node

    def deleteAtTail(self):
        if not self.lastNode:
            return None
        else:
            node=self.lastNode
            prev=self.lastNode.prev
            prev.next=self.firstNode
            self.firstNode.prev=prev
            return node



    def getLength(self):
        return self.size

    def printList(self):
        if not self.firstNode:
            print("Empty List")
        else:
            cur=self.firstNode
            print()
            while(cur.next!=self.firstNode):
                print(cur.val,end=" ")
                cur=cur.next
            print(cur.val,end=" ")

l1=DoublyLinkedList()
l1.insertAtHead(2)
l1.insertAtHead(1)
l1.insertAtTail(3)
l1.printList()
val=l1.deleteAtHead()
print("value of deleted node: ",end=" ")
print(val)
l1.printList()
val=l1.deleteAtTail()
print("value of deleted node: ",end=" ")
print(val)
l1.printList()
'''
l1.insertAtHead(3)
l1.insertAtTail(4)
l1.insertAtTail(5)
l1.printList()
l1.deleteAtHead()
l1.printList()
l1.deleteAtTail()
l1.printList()
print(l1.getLength())
'''
