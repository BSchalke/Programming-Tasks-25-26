"""
TASK: 05 Shopping List

# Skills: Loops, lists
Allow the user to add itemds to a shopping list until they type DONE
When they type DONE, print the list and ask if they want to edit any item.
They should select an item by number and allow them to ammend the item.

TODO:
- Fill in functions
- Add demonstration code under `if __name__ == "__main__":`
"""

def create_shopping():
    shopping = []
    while True:
        item = input("Enter an item of shopping:\t")
        if item.upper() == "DONE":
            break
        shopping.append(item)
    return shopping

def edit_shopping(shopping, index, value):
    try:
        shopping[index] = value
    except IndexError:
        return "Index out of range"

def display_shopping(shopping):
    for i, item in enumerate(shopping):
        print(f"{i+1}:\t{item}")

def main():
    shopping = create_shopping()
    while True:
        display_shopping(shopping)
        edit = input("To edit an item of shopping enter its number or enter x to end:\t")
        if edit.lower() == "x":
            break
        value = input("What would you like to change it to:\t")
        edit_shopping(shopping, int(edit)-1, value)


if __name__ == "__main__":
    main()
