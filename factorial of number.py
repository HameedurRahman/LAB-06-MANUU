
a=int(input("Enter a number="))

def factorial(n):
    if n==0:
        return 1
    else:
        return n*factorial(n-1)

print("The factorial of {0} is {1}".format(a,factorial(a)))
