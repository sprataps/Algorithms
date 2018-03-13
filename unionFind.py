class DisjointSet(object):
    def __init__(self,val,parent=None):
        self.val=val
        self.parent=self
        self.rank=0

class UnionFind(object):
    def __init__(self,sets):
        self.n_elements=0
        self.n_trees=0
        self.values=[]
        self.set_value={}
        for i in sets:
            s=self.add(i)

    def add(self,val):
        s=DisjointSet(val)
        self.values.append(s)
        self.set_value[val]=s
        self.n_elements+=1
        self.n_trees+=1
        return s

    def printSet(self):
        for i in self.values:
            print(i.val,i.parent.val,i.rank)

    def union(self,val1,val2):
        if val1 in self.set_value:
            s1=self.set_value[val1]
        else:
            s1=self.add(val1)

        if val2 in self.set_value:
            s2=self.set_value[val2]
        else:
            s2=self.add(val2)

        s2=self.set_value[val2]
        p_s1=self._findParent(s1)
        p_s2=self._findParent(s2)
        if p_s1.rank<p_s2.rank:
            s1.parent=s2
        elif p_s1.rank>p_s2.rank:
            s2.parent=s1
        else:
            s1.parent=s2
            s2.rank+=1
        self.n_trees-=1

    def findParent(self,val):
        s=self.set_value[val]
        parent= self._findParent(s)
        return parent.val

    def _findParent(self,s1):
        if(s1!=s1.parent):
            s1.parent=self._findParent(s1.parent)
        #print("Parent:",s1.parent.val)
        return s1.parent

    def totalElements(self):
        return self.n_elements

    def totalTrees(self):
        return self.n_trees



arr=[int(x) for x in input("Enter values of disjoind sets:").split()]
U=UnionFind(arr)
U.union(1,3)
U.union(1,5)
U.union(3,8)
(U.printSet())
print(U.findParent(1))
print("Total Elements: ",U.totalElements())
print("Trees: ",U.totalTrees())
print(U.findParent(5))
U.printSet()
