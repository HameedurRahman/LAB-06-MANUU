
a=int(input("Enter the number to find its digit's sum="))
number=a
sum1=0
while(a!=0):
   n=a%10
   sum1+=n
   a=a//10

print("The sum of digit of {0} is {1}".format(number,sum1))
