a=int(input("Enter total seconds : "))
hours=a//3600
minutes=(a%3600)//60
seconds=a%60
print("Time is :",hours,":",minutes,":",seconds)