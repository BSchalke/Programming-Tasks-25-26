"""
TASK: 02 Min Max Finder

# Min/Max Finder
Write a program that:
- Accepts a list of integers.
- Manually finds the min and max (no built-in min/max).
- Includes a function `find_min_max(values)` returning `(min_value, max_value)`.

TODO:
- Fill in functions
- Add demonstration code under `if __name__ == "__main__":`
"""
def find_min(values):
    if len(values) == 0:
        raise ValueError
    min = values[0]
    for i in values:
        if i < min:
            min = i
    return min

def find_max(values):
    if len(values) == 0:
        raise ValueError
    max = values[0]
    for i in values:
        if i > max:
            max = i
    return max


def main():
    nums = []
    while True:
        choice = input("Enter a number or enter x to continue...\t")
        try:
            choice = float(choice)
        except:
            break

        nums.append(choice)
    print(find_min(nums))
    print(find_max(nums))

if __name__ == "__main__":
    main()
