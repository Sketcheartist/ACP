a=int(input("enter first number"))
b=int(input("enter second number"))
c=int(input("enter third number"))
if a<=b and a<=c:
  print("a is smallest")
elif b<=a and b<=c:
  print("b is smallest")
else:
  print("c is smallest")