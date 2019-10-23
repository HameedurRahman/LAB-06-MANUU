
n=int(input("Enter the number of terms="))

x=0
y=1
print("The fibonacci series is here:")
for i in range(0,n):
    print(x,end=" ")
    z=x+y
    x=y
    y=z
