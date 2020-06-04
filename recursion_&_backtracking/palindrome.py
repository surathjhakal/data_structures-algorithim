def palindrome(p):
    if len(p)<1:
        return ''
    elif p[0]!=p[len(p)-1]:
        return False
    else:
        return palindrome(p[1:len(p)-1])


p='madam'
a=palindrome(p)
if a==False:
    print("the number is not palindrome")
else:
    print("the number is palindrome")
