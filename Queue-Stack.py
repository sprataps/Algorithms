'''
Implement the following operations of a queue using stacks.

push(x) -- Push element x to the back of queue.
pop() -- Removes the element from in front of queue.
peek() -- Get the front element.
empty() -- Return whether the queue is empty.
Notes:
You must use only standard operations of a stack -- which means only push to top, peek/pop from top, size, and is empty operations are valid.
Depending on your language, stack may not be supported natively. You may simulate a stack by using a list or deque (double-ended queue), as
 long as you use only standard operations of a stack.
You may assume that all operations are valid (for example, no pop or peek operations will be called on an empty queue).
'''
class MyQueue(object):

    def __init__(self):
        self.inStack=[]
        self.outStack=[]

    def push(self,val):
        self.inStack.append(val)

    def pop(self):
        self.move()
        return (self.outStack.pop())

    def peek(self):
        self.move()
        return (self.outStack[-1])

    def size(self):
        print(len(self.inStack)+len(self.outStack))

    def empty(self):
        if not self.outStack and not self.inStack:
            return True #i.e is empty stack
        else:
            return False


    def move(self):
        if not self.outStack:
            while( self.inStack):
                self.outStack.append(self.inStack.pop())


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
