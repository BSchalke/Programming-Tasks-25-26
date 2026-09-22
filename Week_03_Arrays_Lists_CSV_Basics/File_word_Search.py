"""
TASK: 05 File Word Search

# Skills: File reading, loops, Data mining
Ask user for a filename and a search term. https://sherlock-holm.es/ascii/ is a site that has the entire collection of Sherlock Holmes
Load the file and count how many lines contain the search term

TODO:
- Fill in functions
- Add demonstration code under `if __name__ == "__main__":`
"""

def count_term(filename, search_term):
    with open(filename, "r") as file:
        lines = file.readlines()

    count = 0
    for line in lines:
        if search_term in line:
            count += 1

    return count


def main():
    term = input("Enter a term to be searched in Sherlock:\t")
    print(f"This appears {count_term("cano.txt", term)} times in all of Sherlock!")


if __name__ == "__main__":
    main()
