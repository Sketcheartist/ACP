marital=input("marital status").lower()
gender=input("enter gender").lower()
age=int(input("enter age"))
if marital=="married":
  print("driver is insured")
elif gender=="male" and age>30:
  print("driver is insured")
elif gender=="female" and age>25:
  print("driver is insured")
else:
  print("driver is not insured")