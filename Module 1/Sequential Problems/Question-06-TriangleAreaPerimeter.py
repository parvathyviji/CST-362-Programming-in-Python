a = float(input("Enter side a: "))
b = float(input("Enter side b: "))
c = float(input("Enter side c: "))
p = a + b + c
s = p / 2
a= (s * (s - a) * (s - b) * (s - c))**0.5
print("Perimeter =", p)
print("Area =", a)

#OUTPUT
Enter side a: 3
Enter side b: 4
Enter side c: 5
Perimeter = 12.0
Area = 6.0
