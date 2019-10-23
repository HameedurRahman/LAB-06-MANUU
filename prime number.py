
n=int(input("Enter the number of terms to print prime number="))

print("The prime number are here:")
for val in range(2,n+1): 
        
   if val > 1: 
       for n in range(2, val): 
           if (val % n) == 0: 
               break
       else: 
           print(val,end=" ")
