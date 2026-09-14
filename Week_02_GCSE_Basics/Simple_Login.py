"""
TASK: 06 Simple Login

# Skills: Selection, string comparison
Start with a correct username/password (extend if saved in a text file separately):
- Ask for login
- Print "Welcome" or "Access Denied {number} attempts remaining"
Only allow 3 attempts and close the file

TODO:
- Fill in functions
- Add demonstration code under `if __name__ == "__main__":`
"""

def login(enter_username, enter_password):
    with open("login.txt", "r") as file:
        username,password = file.readlines()
    username = username[:-1]

    if enter_username == username and enter_password == password:
        return True
    else:
        return False

def main():
    attempts = 3
    while attempts > 0:
        enter_username = input("Enter username:\t")
        enter_password = input("Enter password:\t")
        if login(enter_username, enter_password):
            print("Welcome")
            break
        else:
            attempts -= 1
            print(f"Access Denied {attempts} attempts remaining")



if __name__ == "__main__":
    main()
