"""
TASK: 06 Temperature Converter

# Temperature Converter
Build a converter tool:
- Convert Celsius <-> Fahrenheit.
- Provide a looped menu.
- Validate user input.

TODO:
- Fill in functions
- Add demonstration code under `if __name__ == "__main__":`
"""

def celsius_to_fahrenheit(c):
    return (c*(9/5)) + 32

def fahrenheit_to_celsius(f):
    return (f-32) * (5/9)

def main():
    print(f"56 C is {celsius_to_fahrenheit(56)} F")
    print(f"34 F is {fahrenheit_to_celsius(34)} C")


if __name__ == "__main__":
    main()
