class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class Linked_list:
    def __init__(self):
        self.head=None

    def append(self,data):
        new_node=Node(data)
        curr_node=self.head
        if curr_node is None:
            self.head=new_node
        else:
            while curr_node.next is not None:
                curr_node=curr_node.next
            curr_node.next=new_node

    def show(self):
        curr_node=self.head
        while curr_node:
            print(f"{curr_node.data}-->",end="")
            curr_node=curr_node.next
        print()
        
    def reverse(self):
        curr_node=self.head
        prev=None
        while curr_node:
            nxt=curr_node.next
            curr_node.next=prev
            prev=curr_node
            curr_node=nxt
        self.head=prev
        
link1=Linked_list()
link1.append(1)
link1.append(5)
link1.append(7)
link1.append(8)
link1.append(11)
link1.append(12)
link1.show()
link1.reverse()
link1.show()
