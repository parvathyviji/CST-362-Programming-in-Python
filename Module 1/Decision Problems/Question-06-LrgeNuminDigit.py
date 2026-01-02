n=int(input("Enter a two digit number :"))
a=n//10
b=n%10
if a>b:
    print("Largest digit is..",a)
else:
    print("Largest digit is..",b)