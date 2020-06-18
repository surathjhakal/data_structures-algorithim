def selection_sort(l,n):
    mini=n
    for i in range(n+1,len(l)):
        if l[mini] > l[i]:
            mini=i
    l[n], l[mini] = l[mini], l[n]
    if n<(len(l)-1):
        selection_sort(l,n+1)
    else:
        print(l)

l = [75,3,2,8,31,1,2]
n=0
selection_sort(l,n)
