"""
TASK: 05 String Parser

# String Parser
Write a parser that:
- Accepts a sentence from the user.
- Splits it into words manually (not using split()).
- Outputs number of words + list of words.

TODO:
- Fill in functions
- Add demonstration code under `if __name__ == "__main__":`
"""

#This is telling me to do something different than the testing file, I will be completing what the testing file describes
#as otherwise tests would fail

def count_words(sentence):
    is_word = False
    num_words = 0
    for c in sentence:
        if c != " " and is_word == False:
            num_words += 1
            is_word = True
        elif c == " ":
            is_word = False

    return num_words

def is_palindrome(text):
    text = text.lower()
    chars = []
    for c in text:
        if c != " ":
            chars.append(c)

    reverse_chars = []
    for i in range(len(chars)-1, -1, -1):
        reverse_chars.append(chars[i])

    if chars == reverse_chars:
        return True

    return False

def main():
    sentence = input("Enter a sentence:\t")

    word_count = count_words(sentence)
    palin = is_palindrome(sentence)
    print(f"Has {word_count} words")
    if palin:
        print("And is a palindrome")
    else:
        print("And is not a palindrome")


if __name__ == "__main__":
    main()
