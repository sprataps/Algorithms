'''
Implement a Stack in which you can get min element in O(1) time and O(1) space.
'''

class MinStack:
    def __init__(self):
        self.stack=[]
        self.top=-1
        self.min=0
        self.max=0

    def push(self,val):
        if self.top==-1:
            self.min=val
            self.max=val
            self.stack.append(val)

        else:
            if val<self.min:
                self.stack.append(2*val-self.min)
                self.min=val
            elif val>self.max:
                self.stack.append(2*val-self.max)
                self.max=val
            else:
                self.stack.append(val)
        self.top+=1

    def pop(self):
        if self.top<0:
            print("Empty Stack")
        if self.stack[self.top]<self.min:
            self.min=2*self.min-self.stack[self.top]
        elif self.stack[self.top]>self.max:
            self.max=2*self.max-self.stack[self.top]
        self.top-=1

    def getMin(self):
        print(self.min)

    def getMax(self):
        print(self.max)

    def printStack(self):
        for i in range(0,self.top+1):
            print(self.stack[i],end=" ")
class Test:
    def implementStack():
        s=MinStack()
        n=1
        while not(n==0):
            n=int(input("/Push:1 /Pop:2 /Min:3 /Max:4 /exit:0 : "))
            if n==1:
                val=int(input("Enter value: " ))
                s.push(val)
            elif n==2:
                s.pop()
            elif n==3:
                s.getMin()
            elif n==4:
                s.getMax()
            s.printStack()
            print()
if __name__=='__main__':
    Test.implementStack()
