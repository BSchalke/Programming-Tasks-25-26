"""
TASK: 01 2D Grid Manipulator

# Create an NxM grid resolver - https://bk2coady.medium.com/daily-coding-problem-62-bfe0e398247b
- Initialises a grid filled with zeros
- Allows user to "paint" coordinates
- Displays updated grid each time

TODO:
- Fill in functions
- Add demonstration code under `if __name__ == "__main__":`
"""

def create_grid(n,m):
    grid = [[0]*n for _ in range(m)]
    return grid

def display_grid(grid):
    for row in grid:
        for element in row:
            print(element, end=" ")
        print("\n")

def edit_grid(grid, n, m, new_value):
    grid[m][n] = new_value
    return grid

def main():
    grid = create_grid(10,10)
    display_grid(grid)
    while True:
        n = int(input("Enter an x coordinate to change:\t"))
        m = int(input("Enter a y coordinate to change:\t"))
        new = int(input("Enter the new value:\t"))
        grid = edit_grid(grid, n-1, m-1, new)
        display_grid(grid)


if __name__ == "__main__":
    main()
