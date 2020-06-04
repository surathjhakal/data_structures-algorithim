def check(s):
    if len(s)<=1:
        return ''
    elif s[0]>s[1]:
        return False
    else:
        return check(s[1:])

s=[-1,2,3,4]
a=check(s)
if a==False:
    print("list is not sorted")
else:
    print("list is sorted")
