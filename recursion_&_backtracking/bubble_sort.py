def bubble(l,n,a):
    if a<n-1:
        if l[a] > l[a+1]:
            l[a], l[a+1] = l[a+1], l[a]
            bubble(l,n,a+1)
    elif n>1:
        bubble(l,n-1,a)



l=[75,3,2,8,31,1]
n=len(l)
a=0
bubble(l,n,a)
print(l)
