password=input("Enter password :")
length=len(password)
if length<6:
    print("Weak")
elif length<=10:
    print("Medium")
else:
    print("Strong")

#OUTPUT
Enter password :cemp@123clg
Strong
