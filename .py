#linked list creation

#create a node

class Node:   #node creation
    def __init__(self,data):
        self.data=data
        self.next=None
class List:   #linked list making duhhh
    def __init__(self):
        self.head=None
    def append(self,data):   #adding the elements in the code
        new_node=Node(data) #empty list eskitetttt

        if self.head is None:  #if there is nothing in the list
            self.head=new_node
            return
        last=self.head
        while last.next:
            last=last.next
        last.next=new_node

    def display(self):
        current=self.head
        while current:
            print(current.data,end="->")
            current=current.next
        print('None')


# Create a new linked list object
my_list = List()

# Append items to it
my_list.append("i")
my_list.append("have")
my_list.append("lumbago")
my_list.append("6")

my_list.display()

