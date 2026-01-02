a=int(input("Enter first term: "))
d=int(input("Enter common difference: "))
n=int(input("Enter number of terms: "))
temp = a
for i in range(n):
    print(temp)
    temp = temp + d


#OUTPUT
Enter first term: 2
Enter common difference: 3
Enter number of terms: 5
2
5
8
11
14
