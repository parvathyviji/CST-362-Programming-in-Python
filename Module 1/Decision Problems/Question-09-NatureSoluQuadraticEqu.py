a=int(input("Enter a :"))
b=int(input("Enter b :"))
c=int(input("Enter c :"))
d=b*b-4*a*c
if d>0:
    print("Real and distinct roots")
elif d==0:
    print("Real and equal roots")
else:
    print("Imaginary roots")