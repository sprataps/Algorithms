class Node(object):
    def __init__(self,data=None,next=None):
        self.data=data
        self.next_node=next

    def get_data(self):
        return self.data

    def get_next(self):
        return self.next_node

    def set_next(self,new):
        self.next_node=new

class LinkedList(object):

    def __init__(self,head=None):
        self.head=head

    #insert the new node at the head of the linked list
    def insert_at_beginning(self,data):
        new_node=Node(data)
        new_node.set_next(self.head)
        self.head=new_node

    def insert_at_end(self,data):
        new_node=Node(data)
        current=head
        while(current.get_next()!=None):
            current=current.get_next()
        current.set_next(new_node)

    def size(self):
        count=0
        current=self.head
        while current:
            count+=1
            current=current.get_next()
        return count

    def search(self,data):
        current=self.head
        while(current):
            if current.get_data()==data:
                return current
            current=current.get_next()
        raise ValueError("Data not in the List")

    def delete(self,data):
        current=self.head
        previous=None
        found=False
        while (current):
            if current.get_data()==data:
                found=True
            else:
                previous=current
                current=current.get_next()
        #if there is no node in the linked list
        if current is None:
            raise ValueError("Data not in the list")
        #if the node to be deleted is the only node in the linked list
        if previous is None:
            self.head=current.get_next()
        else:
            previous.set_next(current.get_next())
