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

    def __len__(self):
        count=0
        curr_node=self.head
        while curr_node:
            count+=1
            curr_node=curr_node.next
        return count

    def intersection(self,link2):
        len1=len(link1)
        len2=len(link2)
        if len1>=len2:
            diff=len1-len2
            curr_node1=self.head
            curr_node2=link2.head
            while diff:
                diff-=1
                curr_node1=curr_node1.next
            while (curr_node1 and curr_node2):
                if curr_node1.data==curr_node2.data:
                    print(curr_node1.data)
                    break
                curr_node1=curr_node1.next
                curr_node2=curr_node2.next
        else:
            diff=len2-len1
            curr_node1=self.head
            curr_node2=link2.head
            while diff:
                diff-=1
                curr_node2=curr_node2.next
            while (curr_node1 and curr_node2):
                if curr_node1.data==curr_node2.data:
                    print(curr_node1.data)
                    break
                curr_node1=curr_node1.next
                curr_node2=curr_node2.next

link1=Linked_list()
link1.append(3)
link1.append(6)
link1.append(9)
link1.append(15)
link1.append(30)

link2=Linked_list()
link2.append(10)
link2.append(15)
link2.append(30)

link1.intersection(link2)
