"""
TASK: 01 Grade Calculation

# Skills: Input, output, selection
Write a program that asks the user for a percentage grade and prints the corresponding letter grade:
- A: 80-100
- B: 60-79
- C: 40-59
- D: <40
Include a function def get_grade(score):

TODO:
- Fill in functions
- Add demonstration code under `if __name__ == "__main__":`
"""

def get_grade(score):
    boundaries = {"D":39, "C":59, "B":79, "A":100}

    for key in boundaries:
        if  score <= boundaries[key]:
            return key

    return "Invalid percentage"

def main():
    score = float(input("Enter percentage score:\t"))
    print(get_grade(score))


if __name__ == "__main__":
    main()
