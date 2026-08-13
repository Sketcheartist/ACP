import math
n=int(input("enter number:"))
r=int(math.sqrt(n))
prime=True
if r<2:
  prime=False
else:
  for i in range(2,r):
    if r%i==0:
      prime=False
      break
if prime:
  print("square root is prime")
else:
  print("square root is not prime")