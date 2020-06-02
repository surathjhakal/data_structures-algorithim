def reverse(s):
    if len(s)==0:
        return []

    return [s[len(s)-1]] + reverse(s[:len(s)-1])
s=[0,1,2,3,4,5,6,7,8]
print(reverse(s))
print(s[::-1])
