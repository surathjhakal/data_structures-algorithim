def find_sum(s):
    if len(s) == 1:
        print(s)
        return s[0]
    return s[0] + find_sum(s[1:])
s=[1,2,3,4]
print(find_sum(s))
