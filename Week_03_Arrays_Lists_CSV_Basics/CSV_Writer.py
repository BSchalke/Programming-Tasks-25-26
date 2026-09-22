"""
TASK: 01 Csv Writer

# Skills: CSV writing
CAsk the user for:
- Name
- age
- favourite colour
- anything you want
Append this to a CSV file (Extend: allow user to choose to edit the file and read the file)

TODO:
- Fill in functions
- Add demonstration code under `if __name__ == "__main__":`
"""
import csv

def write_csv(filename: str, contents):
    with open(filename, "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerows(contents)


def main():
    data = []
    while True:
        person = []
        name = input("Name(x to exit):\t")
        if name.lower() == "x":
            break
        person.append(name)
        age = input("Age:\t")
        person.append(age)
        fav = input("Favourite Colour:\t")
        person.append(fav)
        hobby = input("Hobby:\t")
        person.append(hobby)
        data.append(person)

    #data = [["Name", "Age", "Favourite colour", "Hobby"]]
    write_csv("people.csv", data)

if __name__ == "__main__":
    main()
