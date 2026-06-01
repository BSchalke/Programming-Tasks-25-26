"""
TASK: 01 Average Calculator

# Average Calculator
Write a Python program that:
- Prompts the user for a list of numbers.
- Stores them in a 1D list.
- Calculates the mean *without using built-in statistics libraries*.
- Includes input validation.
- Implements a reusable function: `calculate_average(values)`.

TODO:
- Fill in functions
- Add demonstration code under `if __name__ == "__main__":`
"""

def calculate_average(values):
    if len(values) == 0:
        raise ValueError

    sum = 0
    for i in values:
        try:
            sum += i
        except TypeError:
            return "Not all values are integer or float type"

    return sum / len(values)

def main():
    nums = []
    while True:
        choice = input("Enter a number to find average or enter x to continue...\t")
        try:
            choice = float(choice)
        except:
            break

        nums.append(choice)
    print(calculate_average(nums))



if __name__ == "__main__":
    main()
