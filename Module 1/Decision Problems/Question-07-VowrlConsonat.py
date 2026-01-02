ch=input("Enter a character :")
if ch in 'aeiouAEIOU':
    print("vowel")
elif (ch>='a' and ch<='z') or (ch>='A' and ch<='Z'):
    print("consonant")
else:
    print("Invalid input")