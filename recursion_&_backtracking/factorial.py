def factorial(n):
    if n==1:
        return 1

    return n*factorial(n-1)
n=5
print("the factorial of {} is {}".format(n,factorial(n)))
