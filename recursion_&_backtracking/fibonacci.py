def fibonacci(n,old,new,c):
    if c>n:
        return ''
    elif c<1:
        print(old,end=' ')
        print(new,end=' ')
        fibonacci(n,old,new,c+1)
    else:
        a=old+new
        print(a,end=' ')
        new, old = a, new
        fibonacci(n,old,new,c+1)
old=0
new=1
c=0
fibonacci(6,old,new,c)

