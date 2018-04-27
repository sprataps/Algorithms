class Node(object):
    def __init__(self,val=None):
        self.val=val
        self.next=None

class LinkedList(object):
    def __init__(self):
        self.head=None

    def insertAtLast(self,val):
        node=Node(val)
        if not self.head:
            self.head=node
            return

        cur=self.head
        while(cur.next):
            cur=cur.next
        cur.next=node
        return

    def insertAtFirst(self,val):
        node=Node(val)
        node.next=self.head
        self.head=node
        return

    def printList(self,head):
        cur=head
        while(cur):
            print(cur.val,end="->")
            cur=cur.next
        print(None)

    def getLength(self,head):
        l=0
        cur=head
        while(cur):
            cur=cur.next
            l+=1
        return l

    def findMiddle(self,head):
        slow=head
        fast=head
        while(fast.next and fast.next.next):
            fast=fast.next.next
            slow=slow.next
        return slow.val

    def sortLinkedList(self):
        self.head=self.mergeSort(self.head)
        return

    def mergeSort(self,ll):
        l=self.getLength(ll)
        if l==0 or l==1:
            return ll
        i=0
        cur=ll
        while(i<int(l/2)-1):
            cur=cur.next
            i+=1
        link2=cur.next
        cur.next=None
        ll1=self.mergeSort(ll)
        ll2=self.mergeSort(link2)
        return self.merge(ll1,ll2)

    def merge(self,l1,l2):
        l=Node(None)
        head=l
        while(l1 and l2):
            if l1.val<l2.val:
                l.next=l1
                l1=l1.next
            elif l1.val>l2.val:
                l.next=l2
                l2=l2.next
            else:
                l.next=l1
                val=l1.val
                while(l1 and l1.val==val):
                    l1=l1.next
                while(l2 and l2.val==val):
                    l2=l2.next
            l=l.next
        l.next=l1 or l2
        self.printList(head.next)
        return head.next

    def mergeRecursive(self,l1,l2):
        if not l1:
            return l2
        if not l2:
            return l1
        if l1.val<l2.val:
            l1.next=self.mergeRecursive(l1.next,l2)
            return l1
        elif l2.val<l1.val:
            l2.next=self.mergeRecursive(l1,l2.next)
            return l2
        else:
            return self.mergeRecursive(l1.next,l2.next)

ll1=LinkedList()
arr=[int(x) for x in input("Enter linkedList: ").split()]
for i in arr:
    ll1.insertAtLast(i)
print(ll1.findMiddle(ll1.head))
