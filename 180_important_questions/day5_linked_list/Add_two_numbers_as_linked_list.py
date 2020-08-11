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
        s=''
        while curr_node:
            s=str(curr_node.data)+s
            nxt=curr_node.next
            curr_node.next=prev
            prev=curr_node
            curr_node=nxt
        self.head=prev
        return s


    def add_two_numbers(self,link1,link2):
        sum2=link2.reverse()
        sum1=link1.reverse()
        total=int(sum1)+int(sum2)
        i=0
        while i<len(str(total)):
            self.append(str(total)[i])
            i+=1
        self.reverse()
        print("The answer of add to linked list is:")

link=Linked_list()

link1=Linked_list()
link1.append(1)
link1.append(5)
link1.append(7)

link2=Linked_list()
link2.append(8)
link2.append(1)
link2.append(1)

link.add_two_numbers(link1,link2)
link.show()
