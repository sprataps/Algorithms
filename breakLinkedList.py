from linked_list_recursive_functions import *

class BreakList(LinkedList):
    def breakList(self,n):
        length=l.length()
        i=0
        list1=self.head
        l2=self.head
        cur=self.head
        while(i<n-1):
            cur=cur.next
            i+=1
        list2=cur.next
        cur.next=None
        print("List1: ")
        cur1=list1
        while(cur1):
            print(cur1.val)
            cur1=cur1.next
        print("List2: ")
        cur2=list2
        while(cur2):
            print(cur2.val)
            cur2=cur2.next


l=BreakList()

l.insertFront(1)
l.insertFront(2)
l.insertFront(3)
l.insertFront(4)
l.insertFront(5)
print(l.length())
print("List to break: ")
l.printList()
l.breakList(3)
