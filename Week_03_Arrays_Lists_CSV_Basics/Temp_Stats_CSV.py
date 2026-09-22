"""
TASK: 04 Temp Stats Csv

# Skills CSV read, simple maths
Go to this site https://www.metoffice.gov.uk/hadobs/hadcet/data/download.html and download the txt file
Daily Mean Temperature.
This file has dates and daily temperatures:
- Read all of the values
- Find the highest, lowest and average
- Print those three values
Extend - See how you can potentially use the dates to chart daily temp changes by years, by months
by day comparisons over time. Maybe chart them using mathplotlib or another library. Just see what you can do with it

TODO:
- Fill in functions
- Add demonstration code under `if __name__ == "__main__":`
"""

def read_data(filename):
    with open(filename, "r") as file:
        data = file.readlines()
    data = data[2:]
    return data

def get_values(data):
    minimum = float(data[0].split()[1].strip("\n"))
    maximum = float(data[0].split()[1].strip("\n"))
    total = 0
    count = len(data)
    for line in data:
        temperature = float(line.split()[1].strip("\n"))
        total += temperature
        if temperature < minimum:
            minimum = temperature
        elif temperature > maximum:
            maximum = temperature
    return minimum, maximum, total/count

def main():
    data = read_data("meantemp_daily_totals.txt")
    minimum, maximum, average = get_values(data)
    print(f"Minimum: {minimum}")
    print(f"Maximum: {maximum}")
    print(f"Average: {average}")

if __name__ == "__main__":
    main()
