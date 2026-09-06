"""
TASK: 04 Linear Search

# Linear Search
Implement a linear search algorithm:
- Ask the user for a target value.
- Search a generated random list.
- Return the index or -1.
- Include `linear_search(values, target)`.

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

def linear_search(values, target):
    for i, value in enumerate(values):
        if value == target:
            return i
    return -1

def main():
    random_list = generate_list()
    print(f"List: {random_list}")
    value = r.randint(0, 10)
    result = linear_search(random_list, value)
    if result == -1:
        print(f"{value} is not in the list")
    else:
        print(f"{value} is in the list at index {result}")


if __name__ == "__main__":
    main()
