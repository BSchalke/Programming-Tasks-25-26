"""
TASK: 03 2D Array Adder

# 2D Array Added
Create a 2D arraw and allow user to:
- Append new values in
- read all current values
- delete a chosen entry

TODO:
- Fill in functions
- Add demonstration code under `if __name__ == "__main__":`
"""

def create_2d(rows:int, columns:int) -> list:
    return [[None] * columns for i in range(rows)]

def edit_2d(array:list, row:int, column:int, value) -> list:
    array[row-1][column-1] = value
    return array

def read_2d(array:list):
    for i in range(len(array)):
        for j in range(len(array[i])):
            print(array[i][j], end=" ")
        print("\n")

def del_2d(array:list, row:int, column:int) -> list:
    array[row-1][column-1] = None
    return array


def main():
    rows = 10
    columns = 10
    array = create_2d(rows, columns)

    array = edit_2d(array, 5, 5, "Middle")
    read_2d(array)


if __name__ == "__main__":
    main()
