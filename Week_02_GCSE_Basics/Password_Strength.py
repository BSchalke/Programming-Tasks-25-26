"""
TASK: 04 Password Strength

# Skills: Strings, loops, selection
Ask the user to enter a password, and check that they meet these conditions:
- At least 8 characters
- Contains a number
- Contains a captial and lower cased letter
- Extend for one special character
Print a response of weak, medium or strong for how many they pass.

TODO:
- Fill in functions
- Add demonstration code under `if __name__ == "__main__":`
"""

def check_password(password: str):
    total = 0

    password_length = False
    if len(password) >= 8:
        password_length = True
        total += 1

    contains_num = False
    contains_cap = False
    contains_lower = False
    contains_special = False

    for i in password:
        if not contains_num and i.isdigit():
            contains_num = True
            total += 1
        elif not contains_cap and i.isupper():
            contains_cap = True
            total += 1
        elif not contains_lower and i.islower():
            contains_lower = True
            total += 1
        elif not contains_special and i in "!£$%^&*(){}[]#~'@;:,<.>?/|`":
            contains_special = True
            total += 1

    if total <= 2:
        return "weak"
    if total <= 4:
        return "medium"
    else:
        return "strong"



def main():
    print(check_password("FreudLovesKids123"))
    print(check_password("ExtremelySecurePassw0rd!"))
    print(check_password("12345"))


if __name__ == "__main__":
    main()
