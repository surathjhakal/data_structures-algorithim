def bubble_sort(l,n):
    for i in range(n-1):
        if l[i] > l[i+1]:
            l[i], l[i+1] = l[i+1], l[i]
    if n>1:
        bubble_sort(l,n-1)
    else:
        print(l)

l = [75,3,2,8,31,1]
n=len(l)
bubble_sort(l,n)
