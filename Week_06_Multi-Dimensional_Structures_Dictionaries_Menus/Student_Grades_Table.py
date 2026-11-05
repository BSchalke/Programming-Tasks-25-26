"""
TASK: 04 Student Grades Table

# Use a dictionary of lists e.g
grades = {
  "Alice": [80, 85, 90],
  "Ben": [70, 60, 75]
}
Add:
- Function to compute class averages
- Function to add student
- Function to remove student

TODO:
- Fill in functions
- Add demonstration code under `if __name__ == "__main__":`
"""

def get_avg(grades):
    total = 0
    count = 0
    for i in grades:
        for j in grades[i]:
            total += j
            count += 1
    return total/count

def add_student(grades, new_student, new_scores):
    grades[new_student] = new_scores
    return grades

def remove_student(grades, student_name):
    grades.pop(student_name)
    return grades

def main():
    grades = {
  	"Alice": [80, 85, 90],
  	"Ben": [70, 60, 75]
	}
    print(get_avg(grades))
    grades = add_student(grades, "Dylan", [1,2,3])
    print(get_avg(grades))
    grades = remove_student(grades, "Alice")
    print(get_avg(grades))

if __name__ == "__main__":
    main()
