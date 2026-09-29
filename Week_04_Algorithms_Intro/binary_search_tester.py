"""
TASK: 02 Binary Search Tester

# Binary Search Tester
Generate a sorted list. Implement:
- iterative binary search
- recursive binary search
Then benchmark them with random inputs.

TODO:
- Fill in functions
- Add demonstration code under `if __name__ == "__main__":`
"""
import random as r
from bubble_sort import bubble_sort

def generate_list(length:int=10, lower_bound:int=0, upper_bound:int=10) -> list:
    final = []
    for i in range(length):
        final.append(r.randint(lower_bound, upper_bound))

    return bubble_sort(final)[0]

def binary_search(items:list, value):
    upper = len(items)-1
    lower = 0
    pointer = len(items)//2
    found = False
    while upper-lower > 1 and not found:
        if items[pointer] == value:
            found = True
        elif items[pointer] > value:
            upper = pointer
        else:
            lower = pointer

        pointer = ((upper-lower)//2) + lower

    if found:
        return pointer+1
    else:
        return -1

def main():
    random_list = generate_list()
    random_value = r.randint(0,10)
    print(f"Random list: {random_list}")
    pointer = binary_search(random_list, random_value)
    if pointer != -1:
        print(f"{random_value} found at index {pointer}")
    else:
        print(f"{random_value} not found")


if __name__ == "__main__":
    main()
