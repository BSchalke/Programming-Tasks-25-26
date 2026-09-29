"""
TASK: 03 Grid Path Counter

# Grid Path Counter - https://bk2coady.medium.com/daily-coding-problem-62-bfe0e398247b
Given an NxM grid:
- Count paths using recursion
- Count paths using iteration
Movement allowed: RIGHT or DOWN only.

TODO:
- Fill in functions
- Add demonstration code under `if __name__ == "__main__":`
"""

# values form pascals triangle, can be found with nCr
# n = (N+M)-2
# r = N or M (doesn't matter)
from math import factorial

def count_paths_recursive(n:int, m:int):
    if n+m == 0:
        return 0
    if n == 1 or m == 1:
        return 1

    return count_paths_recursive(n-1, m) + count_paths_recursive(n, m-1)

def main():
    n = int(input("Enter a value for N:\t"))
    m = int(input("Enter a value for M:\t"))
    print(f"There are {count_paths_recursive(n,m)} different possible paths in this grid")


if __name__ == "__main__":
    main()
