class dequeue:
    def __init__(self):
        self.queue=[]

    def insertFront(self,val):
        self.queue.insert(0,val)

    def insertEnd(self,val):
        self.queue.append(val)

    def deleteFront(self):
        self.queue.pop(0)

    def deleteEnd(self):
        self.queue.pop()

    def printQueue(self):
        print(self.queue)

d=dequeue()
d.insertFront(1)
d.insertFront(2)
d.printQueue()
d.insertEnd(3)
d.printQueue()
d.deleteEnd()
d.printQueue()
