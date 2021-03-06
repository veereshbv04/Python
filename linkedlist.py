class Node:
    def __init__(self,data=None,next=None):
        self.data=data
        self.next=next

class LinkedList:
    def __init__(self):
        self.head=None

    def insert_at_begining(self,data):
        node =Node(data,self.head)
        self.head=node
    
    def insert_at_end(self,data):
        if self.head is None:
            node=Node(data,None)
            self.head=node

        itr=self.head

        while itr.next :
            itr=itr.next

        itr.next=Node(data,None)
    
    def print(self):
        if self.head is None:
            print("Linked List is empty")
            return

        itr=self.head
        listr=" "

        while itr:
            listr+= str(itr.data) + "-->"
            itr =itr.next

        print(listr)

ll=LinkedList()
ll.insert_at_begining(5)
ll.insert_at_begining(45)
ll.print()

