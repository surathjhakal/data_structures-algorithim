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


    #Q3 merge Two sorted linked Linked_list
    def merge(self,link2):
        p=self.head
        q=link2.head
        s=None

        if not p:
            return q
        if not q:
            return p

        if p and q:
            if p.data <= q.data:
                s = p
                p = s.next
            else:
                s = q
                q = s.next
            new_head = s
        while p and q:
            if p.data <= q.data:
                s.next = p
                s = p
                p = s.next
            else:
                s.next = q
                s = q
                q = s.next
        if not p:
            s.next=q
        if not q:
            s.next=p
        return new_head

link1=Linked_list()
link1.append(1)
link1.append(5)
link1.append(7)
link1.append(8)
link1.append(11)
link1.append(12)

link2=Linked_list()
link2.append(2)
link2.append(3)
link2.append(6)
link2.append(10)

link1.merge(link2)
link1.show()
