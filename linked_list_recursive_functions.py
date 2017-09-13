class Node:
    def __init__(self,val,next=None):
        self.val=val
        self.next=next

    def __str__(self):
        return str(self.val)

class LinkedList:
    def __init__(self,val):
        self.head=Node(val)

    def getNext(self):
        return self.next

    def setNext(self,val):
        self.next=Node(val)

    def printList(self):
        if not self.head:
            return None
        else:
            self._printList(self.head)

    def _printList(self,node):
        if not node:
            return None
        else:
            print(node)
            self._printList(node.next)
    def sum(self):
        if not self.head:
            return 0
        else:
            self._sum(self.head)
    def  _sum(self,node):
        if not node:
            return 0
        else:
            return node.val+(self._sum(node.next))
    def length(self):
        if not self.head:
            return 0
        else:
            self._length(self.head)
    def _length(self,node):
        if not node:
            return 0
        else:
            return 1+(self._length(node.next))
    def reversePrint(self):
        if not self.head:
            return None
        else:
            self._reverse(self.head)
    #print the next node first and then print the current node
    def _reversePrint(self,node):
        if not node:
            return None
        else:
            self._reversePrint(node.next)
            print(node)

    def search(self,value):
        if not self.head:
            return None
        else:
            self._search(self.head,value)
    def _search(self,node,value):
        if not node:
            return None
        elif node.val==value:
            return True
        else:
            self._search(node.next,value)
    def insertRear(self,value):
        if not self.head:
            return Node(value)
        else:
            self._insertRear(self.head,value)
    def _insertRear(self,node,value):
        if not node.next:
            return node.next=Node(value)
        else:
            self._insertRear(node.next,value)
    def deleteFirst(self):
        if not self.head:
            return None
        elif not self.head.next:
            return None
        else:
            self.head.next=self.head.next.next
            return self.head

    def reverseList(self):
        if not self.head:
            return None
        else:
            self._reverseList(self.head)
    def _reverseList(self,node):
        if not node:
            return None:
        else:
