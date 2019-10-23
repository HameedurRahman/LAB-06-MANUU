
n=input("Enter a string=")

m=reversed(n)

if list(n)==list(m):
    print("{0} is a palindrome string".format(n))
else:
    print("{0} is not a palindrome string".format(n))

