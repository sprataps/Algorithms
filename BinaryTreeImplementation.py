from collections import deque
class Node(object):
    def __init__(self,val,left=None,right=None):
        self.val=val
        self.left=left
        self.right=right

class BinaryTree(object):
    def __init__(self):
        self.root=None

    def insert(self,val):
        if not(self.root):
            self.root=Node(val)

        else:
            self._insert(val)

    def  _insert(self,val):
        node=Node(val)
        stack=deque([self.root])
        while(stack):
            root=stack.pop()
            if root:
                if not(root.left):
                    root.left=node
                    #print("left inserted to:",root.val," Inorder: ",self.inorder())
                    return

                if not(root.right):
                    root.right=node
                    #print("right Inserted to:",root.val,"Inorder: ",self.inorder())
                    return

                if root.left:
                    stack.appendleft(root.left)
                if root.right:
                    stack.appendleft(root.right)



    def printTree(self):
        if not self.root:
            return None
        print("Inorder: ",self.inorder())
        print("Preorder:",self.preorder())
        print("Postorder:",self.postorder())
        print("LevelOrder:",self.levelorder())

    def inorder(self):
        stack=[]
        ret=[]
        root=self.root
        while(stack or root):
            while(root):
                stack.append(root)
                root=root.left
            root=stack.pop()
            ret.append(root.val)
            root=root.right
        return ret

    def preorder(self):
        stack=[]
        ret=[]
        root=self.root
        while(stack or root):
            if root:
                ret.append(root.val)
                stack.append(root.right)
                stack.append(root.left)
            root=stack.pop()
        return ret

    def postorder(self):
        stack=[]
        ret=[]
        last=None
        root=self.root
        while(stack or root):
            if (root):
                stack.append(root)
                root=root.left
            else:
                if stack[-1] and stack[-1].right and stack[-1].right!=last:
                    root=stack[-1].right
                else:
                    last=stack.pop()
                    ret.append(last.val)
        return ret

    def levelorder(self):
        stack=[[self.root]]
        ret=[]
        while(stack[0] or root):
            ret.append([node.val for node in stack[0]])
            stack1=[]
            for node in stack[0]:
                if node.left:
                    stack1.append(node.left)
                if node.right:
                    stack1.append(node.right)
            if stack1:
                stack[0]=stack1
            else:
                break
        return ret

    def height(self):
        if not self.root:
            return 0
        print("Height:", self.iterativeHeight())

    def _height(self,root):
        if not root:
            return 0
        return 1 + max( self._height(root.left) , self._height(root.right))

    def _heightII(self,root,h):
        if not root:
            return h
        leftHeight= self._heightII(root.left,1+h)
        rightHeight= self._heightII(root.right,1+h)
        return max(leftHeight,rightHeight)

    def iterativeHeight(self):
        if not self.root:
            return 0
        q=deque()
        q.append([self.root])
        height=1
        while(q):
            stack=[]
            for root in q[0]:
                if root.left:
                    stack.append(root.left)
                if root.right:
                    stack.append(root.right)
            if stack:
                q[0]=stack
                height+=1
            else:
                break
        return height

    def breadthFirstSearch(self):
        print("BFS:")
        print( self.levelorder())

    def depthFirstSearch(self):
        print("DFS:")
        print( self.preorder())
    '''
    Print all paths from root to leafs
    '''
    def printPathsRecursive(self):
        if not self.root:
            return
        ( self._printPathsRecursive(self.root,''))

    def _printPathsRecursive(self,tree,s):

        if not tree:
            return s

        if not tree.left and not tree.right:
            if len(s)!=0:
                return (s+str(tree.val))
        leftPath= ( self._printPathsRecursive(tree.left, s+str(tree.val)+"->"))
        rightPath= ( self._printPathsRecursive(tree.right, s+str(tree.val)+"->"))
        if leftPath:
            print(leftPath)
        if rightPath:
            print(rightPath)


   #BFS using queue
    def printPathsIterativeI(self):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        if not self.root:
            return []
        ret=[]
        queue=deque()
        queue.append([self.root, ""])
        while(queue):
            node,path=queue.popleft()
            if not(node.left)  and not(node.right):
                ret.append(path+str(node.val))
            if node.right:
                queue.append([node.right,path+str(node.val)+"->"])
            if node.left:
                queue.append([node.left,path+str(node.val)+"->"])
        print( ret)

    #DFS using stack
    def printPathsIterativeII(self):
        if not self.root:
            return []
        ret,stack=[],[[self.root,""]]
        while(stack):
            node,path=stack.pop()
            if not(node.left) and not(node.right):
                ret.append(path+str(node.val))
            if node.right:
                stack.append([node.right,path+str(node.val)+"->"])
            if node.left:
                stack.append([node.left,path+str(node.val)+"->"])
        return ret


    '''
    Calculate if there is a path whose values sum up to given value
    '''

    def pathSumRecursive(self,target):
        if not self.root:
            return False
        (self._pathSumRecursive(self.root,target,""))

    def _pathSumRecursive(self,node,target,s):
        if not(node) and target==0:
            return s
        if not(node) and target!=0:
            return None
        if not(node.right) and not(node.left) and target==node.val:
            return s+str(node.val)
        leftSubtree=self._pathSumRecursive(node.left,target-node.val,s+str(node.val)+"->")
        rightSubtree=self._pathSumRecursive(node.right,target-node.val,s+str(node.val)+"->")

        if leftSubtree:
            print(leftSubtree)
        if rightSubtree:
            print(rightSubtree)

    #DFS using stack
    def pathSumIterativeI(self,target):
        if not self.root and target==0:
            return True
        if not self.root and target!=0:
            return False
        ret,stack=[],[[self.root,target,""]]
        while(stack):
            node,target,path=stack.pop()
            if not(node.left) and not(node.right) and target-node.val==0:
                ret.append(path+str(node.val))
            if node.right:
                stack.append([node.right,target-node.val,path+str(node.val)+"->"])
            if node.left:
                stack.append([node.left,target-node.val,path+str(node.val)+"->"])
        print(ret)

    def pathSumIterativeII(self,target):
        if not self.root and target==0:
            return True
        if not self.root and target!=0:
            return False
        ret=[]
        queue=deque()
        queue.append([self.root,target-self.root.val,str(self.root.val)])
        while(queue):
            node,target,path=queue.popleft()
            if not(node.left) and not(node.right) and target==0:
                ret.append(path)
            if node.left:
                queue.append([node.left,target-node.left.val,path+"->"+str(node.left.val)])
            if node.right:
                queue.append([node.right,target-node.right.val,path+"->"+str(node.right.val)])
        print(ret)




bt=BinaryTree()
arr=[1,2,3,4,5,6,7,8,9,10]
for i in arr:
    bt.insert(i)
bt.printTree()
#bt.height()
#bt.breadthFirstSearch()
#bt.depthFirstSearch()
#bt.printPathsRecursive()
#bt.printPathsIterativeII()
bt.pathSumIterativeI(18)
