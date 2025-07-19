import re

password = input("Enter a password")

length_ok = len(password) >= 8
upper_ok = re.search(r'[A-Z]', password)
lower_ok = re.search(r'[a-z]',password)
digit_ok = re.search(r'\d', password)
special_ok = re.search(r'[!@#$%^&*(),.?":{}|<>]', password)

if length_ok and upper_ok and lower_ok and digit_ok and special_ok:
    print("Strong Password")
else:
    print("Week Password . Make sure it has: ")
    if not length_ok:
        print("- At least 8 characters")
    if not upper_ok:
        print("- At least one uppercase letter")
    if not lower_ok:
        print("- At least one lowercase letter")
    if not digit_ok:
        print("- At least one digit")
    if not special_ok:
        print("- At least one special character (!@#$ etc.)")