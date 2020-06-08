def upper(s):
    if len(s)<1:
        print('not found')
    elif s[0]==s[0].upper():
        print(s[0])
    else:
        upper(s[1:])

s='helloI'
upper(s)
