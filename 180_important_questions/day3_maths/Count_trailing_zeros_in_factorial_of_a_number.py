def trailing(n):
    count=0
    i=5
    while (n/i>=1):
        count += int(n/i)
        i*= 5
    print(count)

def main():
    n=int(input("Enter a number:"))
    trailing(n)

main()
