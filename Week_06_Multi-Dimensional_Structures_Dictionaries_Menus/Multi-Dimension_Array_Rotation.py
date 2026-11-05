"""
TASK: 03 Multi-Dimension Array Rotation

# Rotate a 2D matrix 90 degrees clockwise manually
Good luck

TODO:
- Fill in functions
- Add demonstration code under `if __name__ == "__main__":`
"""

def transpose(matrix):
    final = [[None]*len(matrix) for _ in range(len(matrix[0]))]
    for i, row in enumerate(matrix):
        for j, element in enumerate(row):
            final[j][i] = element

    return final

def reverse(matrix):
    for i, row in enumerate(matrix):
        matrix[i] = row[::-1]
    return matrix

def rotate_matrix(matrix):
    return reverse(transpose(matrix))

def main():
    matr = [[1,2,3,4],[5,6,7,8]]
    print(rotate_matrix(matr))


if __name__ == "__main__":
    main()
