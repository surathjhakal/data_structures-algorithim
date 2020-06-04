def binary_search(list1,search,low,high):
    if high>=low:
        mid = (low + high) // 2
        if list1[mid]==search:
            return True
        elif list1[mid]<search:
            return binary_search(list1,search,mid+1,high)
        elif list1[mid]>search:
            return binary_search(list1,search,low,mid-1)
    else:
        return False

list1=[2,23,45,65,87,91,98]
search=92
low=0
high=7
a=binary_search(list1,search,low,high)
if a:
    print("number found")
else:
    print("number not found")
