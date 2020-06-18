def binary_search(list1,search):
    if len(list1)==0:
        return False
    else:
        mid=len(list1)//2
        if list1[mid]==search:
            return True
        else:
            if list1[mid]>search:
                return binary_search(list1[:mid],search)
            else:
                return binary_search(list1[mid+1:],search)

list1=[2,23,45,65,87,91,98]
search=91
a=binary_search(list1,search)
if a:
    print("number found")
else:
    print("number not found")
