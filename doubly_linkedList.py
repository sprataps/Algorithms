from NodeClass import Node

class DoublyLinkedList:
    def __init__(self):
        self.head=None
        self.tail=None
        self.size=0

    def insertAtHead(self,val):
        temp=Node(val)
        if not self.head:
            self.head=temp
            self.tail=temp
        else:
            temp.next=self.head
            self.head.prev=temp
            temp.prev=None
            self.head=temp
            self.size+=1

    def insertAtTail(self,val):
        temp=Node(val)
        if not self.tail:
            self.tail=temp
        else:
            self.tail.next=temp
            temp.prev=self.tail
            temp.next=None
            self.tail=temp
            self.size+=1

    def deleteAtHead(self):
        if not self.head:
            return None
        temp=self.head
        self.head=self.head.next
        self.head.prev=None
        return temp

    def deleteAtTail(self):
        if not self.tail:
            return None
        else:
            temp=self.tail
            self.tail=self.tail.prev
            self.tail.next=None
            return temp

    def printListFromFront(self):
        if not self.head:
            print("Empty List")
        else:
            cur=self.head
            print()
            while(cur):

                print(cur.val,end=" ")
                cur=cur.next

    def printListBackWards(self):
        if not self.tail:
            print("Empty List")
        else:
            cur=self.tail
            print()
            while(cur):
                print(cur,end=" ")
                cur=cur.prev



l1=DoublyLinkedList()
l1.insertAtHead(2)
l1.insertAtHead(1)
l1.insertAtTail(3)
l1.insertAtTail(4)
l1.printListFromFront()
l1.printListBackWards()
l1.deleteAtHead()
l1.printListFromFront()
l1.deleteAtTail()
l1.printListBackWards()
