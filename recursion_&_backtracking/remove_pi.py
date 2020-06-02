def remove(a):
    new=''
    if len(a)<=1:
        return ''
    elif a[0]=='p' and a[1]=='i':
        print('3.14',end='')
        return remove(a[2:])
    else:
        print(a[0],end='')
        return remove(a[1:])
a='pippppiiiipi'
remove(a)
