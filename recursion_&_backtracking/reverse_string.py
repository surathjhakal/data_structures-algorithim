def reverse(s):
    if len(s)==0:
        return

    a=s[len(s)-1]
    print(a,end='')
    reverse(s[:len(s)-1])

s='hello'
reverse(s)
