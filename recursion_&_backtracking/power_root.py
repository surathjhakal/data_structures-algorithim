def pow(n,p):
    if p==0:
        return 1
    return n*pow(n,p-1)

n=2
p=2
print(pow(n,p))
