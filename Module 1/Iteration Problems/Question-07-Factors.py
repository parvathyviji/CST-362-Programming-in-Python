n = int(input("Enter a number: "))
print("Factors of", n, "are:")
for i in range(1, n + 1):
    if n % i == 0:
        print(i)

#OUTPUT
Enter a number: 25
Factors of 25 are:
1
5
25
