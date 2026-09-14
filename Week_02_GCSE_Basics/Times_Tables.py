"""
TASK: 02 Times Tables

# Skills: Loops,input validation
Ask the user for a number, print the multiplication from 1 to 12 in a readable format:

Extend by using a function you can call for easy entry

TODO:
- Fill in functions
- Add demonstration code under `if __name__ == "__main__":`
"""

def times_table(num):
    multiples = []
    for i in range(1,13):
        multiples.append(num*i)
    return multiples

def main():
    num = int(input("Enter an integer:\t"))
    print(times_table(num))


if __name__ == "__main__":
    main()
