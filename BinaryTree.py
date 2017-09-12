'''
Implementation of a Binary Tree.
Inorder and postorder traversal
'''
class Tree_Node:
    def __init__(self,val=None,left=None, right=None):
        self.val=val
        self.left=left
        self.right=right

    def __str__(self):
        return str(self.val)

    def getLeft(self):
        return str(self.left)

    def getRight(self):
        return str(self.right)

class BinaryTree:
    def __init__(self):
        val=int(input("Enter the value of the root node: "))
        tree=Tree_Node(val)
        self.root=tree
        self.size=1

    def insert(self,val):
        if self.root==None:
            self.root=Tree_Node(val)
            self.size+=1
        else:
            self._insert(self.root,val)

    def _insert(self,root,val):
        if val<=root.val:
            if root.left:
                self._insert(root.left,val)
            else:
                root.left=Tree_Node(val)
                self.size+=1
        if val>=root.val:
            if root.right:
                self._insert(root.right,val)
            else:
                root.right=Tree_Node(val)
                self.size+=1
    def inorder(self):
        print("Inorder Traversal: ")
        if self.root==None:
            print ("Empty Tree.")
            return
        else:
            self._inorder(self.root)

    def _inorder(self,node):
        if node==None:
            return
        self._inorder(node.left)
        print(node.val)
        self._inorder(node.right)
    def postorder(self):
        print("Postorder traversal: ")
        if self.root==None:
            print ("Empty Tree.")
            return
        else:
            self._postorder(self.root)
    def _postorder(self,node):
        if node==None:
            return
        self._postorder(node.right)
        print(node.val)
        self._postorder(node.left)

    def getSize(self):
        return str(self.size)



def main():
    s=[int(x) for x in input("Enter the list of numbers: ").split()]
    tree1=BinaryTree()
    for x in s:
        tree1.insert(x)
    tree1.inorder()
    tree1.postorder()
    print("Size of the tree is: "+tree1.getSize())

if __name__=="__main__":
    main()
