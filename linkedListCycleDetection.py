'''
This is the cylic linked list implementation .
Algorithm uses the floyd's hare and tortoise algorithm to find if the cycle exists
Entry point of the cycle in the linked list is returned
'''

class Node(object):
    def __init__(self,val,next=None):
        self.val=val
        self.next=next

class LinkedList(object):
    def __init__(self):
        self.head=None
        self.length=0

    def insertBehind(self,val,next=None):
        node=Node(val,next)
        if not(self.head):
            self.head=node
            self.length=1
            return
        temp=self.head
        while(temp.next):
            temp=temp.next
        temp.next=node
        self.length+=1

    def insertFront(self,val,next=None):
        node=Node(val,next)
        node.next=self.head
        self.head=node
        self.length+=1


    def deleteFront(self):
        node=self.head
        if self.head.next:
            self.head=self.head.next
            self.length-=1
        else:
            self.length=0
            return None

    def deleteLast(self):
        if self.length==0:
            return
        temp=self.head
        while(temp.next):
            prev=temp
            temp=temp.next
        prev.next=None
        self.length-=1
        print("Deleting: ",temp.val)

    def formCycle(self,entryVal):
        begin=self.head
        while(begin.val!=entryVal):
            begin=begin.next
        end=begin

        while(end.next):
            end=end.next
        end.next=begin


    def printList(self):
        if self.length%2==0:
            print("Will meet at entry")
        else:
            print("Will meet at last node")
        temp=self.head
        prev=temp
        d={}
        slow=self.head
        fast=self.head
        while(temp):
            slow=slow.next
            fast=fast.next.next
            print("Slow: ",slow.val," Fast: ",fast.val)
            if temp.val not in d:
                d[temp.val]=1
                #print(temp.val,end='->')
                temp=temp.next
            if fast==slow:
                print("Met: ",fast.val)
            #else:
            #    print("The list cycle begins at: ",temp.val)
            #    print("Slow: ",slow.val," and fast: ",fast.val)

                return

    def cycleLength(self):
        slow=self.head
        fast=self.head
        dist=0
        while(True):
            slow=slow.next
            fast=fast.next.next
            if slow==fast:
                break
            dist+=1

        print("Nodes travelled before meeting by slow:",dist)
        print("Nodes between head and start of cycle(both inclusive): ",self.length-dist)
        i=1
        temp=self.head
        while(i<self.length-dist):
            temp=temp.next
            i+=1
        print("Cycle starts at: ",temp.val)


ll=LinkedList()
while(True):
    i=int(input())
    if i==-1:
        break
    ll.insertBehind(i)

val=int(input("Entry point of cycle: "))
ll.formCycle(val)
ll.cycleLength()
