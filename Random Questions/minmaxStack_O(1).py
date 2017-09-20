'''
Implement a Stack in which you can get min element in O(1) time and O(1) space.
Two things to see here:
1) if the value we are inserting is lesser than min, if it is it must be inserted in a way that should reflect its minimum value when we
pop it out. this is acheived using the equation that 2(val)-previousminValue < val if val < previousMinValue
2) if we are poppint out the minimum value, then the min value must be updated to the previous min Value that was inserted before the min
Value. This is achieved by 2(presentMinValue)-(popping value(if lesser than min)). this actually cancels out the term with coefficient 2 
in both the equations 1 and 2 and leaves us with previousMinValue from equation1.

The same logic goes for implementing the max value.

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
