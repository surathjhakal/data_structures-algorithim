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

    def palindrome(self):
        curr_node=self.head
        s=[]
        while curr_node:
            s.append(curr_node.data)
            curr_node=curr_node.next

        check=True
        while len(s)>1:
            if s.pop(0)!=s.pop():
                check=False
                break
        if check:
            print("it is palindrome")
        else:
            print("it is not palindrome")

link1=Linked_list()
link1.append(4)
link1.append(1)
link1.append(8)
link1.append(1)
link1.append(4)

link1.show()
link1.palindrome()
