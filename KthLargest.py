class Node(object):
    def __init__(self,val,parent=None,count=None,left=None,right=None):
        self.val=val
        self.parent=parent
        self.left=left
        self.right=left
        self.count=0

class KthLargest(object):

    def __init__(self, k, nums):
        """
        :type k: int
        :type nums: List[int]
        """
        self.root=None
        self.n_nodes=0
        for i in nums:
            self.insert(i)
        self.k=k


    def add(self, val):
        """
        :type val: int
        :rtype: int
        """
        self.insert(val)

        stack=[self.root]

        if self.k>self.n_nodes:
            print("Not enough nodes in Tree!.")
            return None

        while(stack):
            node=stack.pop()
            if node and node.count==self.k:
                return node.val
            if node and node.count<self.k and node.left:
                stack.append(node.left)
            else:
                if node and node.right:
                    stack.append(node.right)
        return None

    def printTree(self):
        queue=collections.deque()
        if not self.root:
            return None
        ret=[]
        queue.append(self.root)
        while(queue):
            node=queue.popleft()
            ret.append([node.val,node.count])
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        print(ret)


    def insert(self,val):
        node=Node(val)

        if not self.root:
            self.root=node
            self.root.parent=self.root
            self.root.count=1
            self.n_nodes=1
            return

        cur=self.root
        flag=0
        left=[]
        while(True):
            if cur.val==val:
                flag=1
                print("Value: "+str(val)+" already exists in the tree!")
                return

            if cur.val<val:
                left.append(cur)
                cur.count+=1
                if cur.right:
                    cur=cur.right
                else:
                    cur.right=node
                    node.count=cur.count-1
                    self.n_nodes+=1
                    break
            else:
                if cur.left:
                    cur=cur.left
                else:
                    cur.left=node
                    node.count=cur.count+1
                    self.n_nodes+=1
                    break
        if flag==0:
            self.increaseCountLeft(left[0] )
        self.printTree()

    def increaseCountLeft(self,node):
        if node.left:
            node=node.left
        else:
            return
        queue=collections.deque()
        queue.append(node)
        while(queue):
            node=queue.popleft()
            if node:
                node.count+=1
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)



        #self.n_nodes+=1
        #self.printTree()



# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)
