def gcd(a,b):
    if (b == 0):
         return a
    return gcd(b, a%b)

def main():
    a =int(input("enter a number"))
    b =int(input("Enter next number"))
    if(gcd(a, b)):
        print('GCD of', a, 'and', b, 'is', gcd(a, b))
    else:
        print('not found')

main()
