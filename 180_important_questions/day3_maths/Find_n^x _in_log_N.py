def find(x,n):
    total=1
    power=n
    while(power):
        if (power%2)==1:
            total*= x
            power-=1
        else:
            x*=x
            power/=2
    if n>0:
        print(f'The square root of number is:{total}')
    else:
        print(f'The square root of number is:{1/total}')

def main():
    x=int(input("Enter the number:"))
    n=int(input("Enter the power of number:"))
    find(x,n)
main()
