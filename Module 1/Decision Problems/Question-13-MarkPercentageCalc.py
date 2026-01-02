p=float(input("Enter percentage: "))
if p >= 90:
    grade = "O (Outstanding)"
elif p >= 85:
    grade = "A+ (Excellent)"
elif p >= 80:
    grade = "A (Very Good)"
elif p >= 70:
    grade = "B+ (Good)"
elif p >= 60:
    grade = "B (Above Average)"
elif p >= 50:
    grade = "C (Average)"
elif p >= 45:
    grade = "P (Pass)"
else:
    grade = "F (Fail)"
print("Percentage is", p)
print("Grade is", grade)

#OUTPUT
Enter percentage: 78
Percentage is 78.0
Grade is B+ (Good)
