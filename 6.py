x=float(input("enter x"))
n=int(input("enter number of terms"))
fact=1
power=1
sign=1
s=1
for i in range(1,n):
  power*=x*x
  fact*=(2*i-1)*(2*i)
  sign*=-1
  s+=sign*power/fact
print("cos(x)=",s)