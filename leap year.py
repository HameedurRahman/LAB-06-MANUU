
a=int(input("Enter any year what you want="))

if a%100:
      if a%400:
          print("{0} is a leap year".format(a))
      else:
          print("{0} is not a leap year".format(a))

else:
      if a%4:
          print("{0} is a leap year".format(a))
      else:
          print("{0} is not a leap year".format(a))
