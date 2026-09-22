"""
TASK: 02 Dice Roll

# Skills: RNG, Loops
Simulate rolling a six-sided die X number of times:
Print each roll, store all values in a list of updated totals for each number (56 ones for example):
Allow the user to print:
- Totals for each side
- average dice roll
- Counts for each of the 6 sides
- Extend (look up how to use mathplotlib and produce a bar graph for all of the statistics)

TODO:
- Fill in functions
- Add demonstration code under `if __name__ == "__main__":`
"""
import random as r

def roll(number:int):
    totals = {1:0, 2:0, 3:0, 4:0, 5:0, 6:0}
    for i in range(number):
        random_roll = r.randint(1,6)
        print(random_roll, end=" ")
        totals[random_roll] += 1
    print("\n")
    return totals

def find_avg(totals:dict):
    avg = (totals[1] + 2*totals[2] + 3*totals[3] + 4*totals[4] + 5*totals[5] + 6*totals[6]) / (totals[1]+totals[2]+totals[3]+totals[4]+totals[5]+totals[6])
    return avg

def main():
    number = int(input("Number of rolls:\t"))
    totals = roll(number)
    for i in totals:
        print(f"{i}: {totals[i]} times")

    print(f"Average: {find_avg(totals)}")


if __name__ == "__main__":
    main()
