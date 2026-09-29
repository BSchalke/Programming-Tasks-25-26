"""
TASK: 01 Bubble Sort

# Bubble Sort
Implement Bubble Sort on any size list:
- Do not use built-in sort()
- Count swaps
- Extend by

TODO:
- Fill in functions
- Add demonstration code under `if __name__ == "__main__":`
"""

def bubble_sort(items:list) -> tuple:
    count = 0
    items = items.copy()

    for i in range(len(items)):
        for j in range(len(items)-1):
            if items[j] > items[j+1]:
                count += 1
                temp = items[j]
                items[j] = items[j+1]
                items[j+1] = temp

    return items,count


def main():
    items = []
    while True:
        try:
            value = float(input("Enter a number:\t"))
            items.append(value)
        except ValueError:
            break

    sorted = bubble_sort(items)
    print(f"Original list: {items}")
    print(f"Sorted list: {sorted[0]}")
    print(f"With {sorted[1]} swaps")


if __name__ == "__main__":
    main()
