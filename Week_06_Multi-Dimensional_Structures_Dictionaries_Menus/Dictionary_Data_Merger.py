"""
TASK: 02 Dictionary Data Merger

# Please refer to the python file with dictionaries in
Given two dictionaries:
- Merge them by summing matching keys
- Present them to the user

TODO:
- Fill in functions
- Add demonstration code under `if __name__ == "__main__":`
"""

def sum_dicts(d1, d2):
    final = {}
    for i in d1:
        if i in d2 and i not in final:
            final[i] = d1[i] + d2[i]
        elif i not in final:
            final[i] = d1[i]
    for i in d2:
        if i not in final:
            final[i] = d2[i]
    return final

def main():
    # I have no idea what your asking me to do so this is what your getting (especially with whatever that is in the other file how can i sum matching keys with no matching keys)
    dict1 = {"Apples": 5, "Milk": 10, "Something else": 2}
    dict2 = {"Apples": 1, "Goo": 9, "Milk": 22}
    print(sum_dicts(dict1, dict2))


if __name__ == "__main__":
    main()
