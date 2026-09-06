"""
TASK: 03 Array Reversal

# Array Reversal
Create a program that:
- Generates a list of random integers.
- Reverses the list manually (no slicing or .reverse).
- Includes a function `reverse_list(values)` that returns a new reversed list.

TODO:
- Fill in functions
- Add demonstration code under `if __name__ == "__main__":`
"""
import random as r

def generate_list(length=10, lower=0, upper=10):
    random_list = []
    for i in range(length):
        random_list.append(r.randint(lower, upper))
    return random_list

def reverse_array(array):
    final = []
    for i in range(len(array)-1, -1, -1):
        final.append(array[i])
    return final

def main():
    array = generate_list()
    print(f"Random list: {array}")
    reversed_array = reverse_array(array)
    print(f"Reversed list: {reversed_array}")


if __name__ == "__main__":
    main()
