#Input : abc
#Output : [abc,acb,bac,bca,cab,cba]

def permute(s):
    output = []

    if len(s) <= 1:
        output = [s]
    else:
        print('s:{}'.format(s))
        for i, let in enumerate(s):
            print(let)
            for perm in permute(s[:i] + s[i + 1:]):
                print('perm is',perm)
                output += [let + perm]
                print('output:{}'.format(output))
    return output
s='abc'
print(permute(s))
