"""
TASK: 01 File Stats Tool

# Read a .txt file and compute:
Task:
- Number of lines
- Number of words
- Number of characters
- Most frequent word

TODO:
- Fill in functions
- Add demonstration code under `if __name__ == "__main__":`
"""

def compute_txt(filename):
    with open(filename, "r") as file:
        lines = file.readlines()
    no_lines = len(lines)
    no_words = 0
    no_chars = 0
    words = {}

    for line in lines:
        no_words += len(line.split())
        no_chars += len(line)
        line_words = line.split()
        for word in line_words:
            if word in words:
                words[word] += 1
            else:
                words[word] = 1

    most = ("", 0)
    for word in words:
        if words[word] > most[1]:
            most = (word, words[word])

    return no_lines, no_words, no_chars, most

def main():
    lines, words, chars, most = compute_txt("words.txt")
    print(f"{lines} lines")
    print(f"{words} words")
    print(f"{chars} characters")
    print(f"{most[0]} is the most frequent word used {most[1]} times")


if __name__ == "__main__":
    main()
