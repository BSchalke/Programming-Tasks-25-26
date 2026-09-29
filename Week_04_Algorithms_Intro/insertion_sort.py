"""
TASK: 03 Insertion Sort

# Insertion Sort Tester
Generate an unsorted list (maybe use RNG). Implement:
- Insertion sort without using inbuild sorts
- Count number of comparions
Then benchmark them with random inputs.

TODO:
- Fill in functions
- Add demonstration code under `if __name__ == "__main__":`
"""
import random as r

def unsorted_list(length=10, lower=0, upper=100):
    final = []
    for i in range(length):
        final.append(r.randint(lower,upper))

    return final

def insertion(array):
    count = 0
    if len(array) <= 1:
        return array, 0
    for i in range(1, len(array)):
        key = array[i]
        j = i - 1
        while j >= 0 and key < array[j]:
            array[j + 1] = array[j]
            j -= 1
            count += 1
        array[j + 1] = key

    return array,count


def main():
    unsorted = unsorted_list()
    print(f"Unsorted: {unsorted}")
    array,count = insertion(unsorted)
    print(f"Sorted: {array}")
    print(f"Comparisons: {count}")


if __name__ == "__main__":
    main()
