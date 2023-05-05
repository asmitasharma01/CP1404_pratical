import csv
from Practical_06 import guitar

# Data to be written to the file
data = [
    ["Fender Stratocaster", 2014, 765.4],
    ["Gibson L-5 CES", 1922, 16035.4],
    ["Line 6 JTV-59", 2010, 1512.9],
    ["Martin Grand J12-16GTE", 2015, 2199],
    ["Taylor PS10ce", 2014, 9318],
    ["Gretsch 6120 Chet Atkins", 1956, 10999.99],
    ["Mambo J7", 1999, 16475.25],
]

class_guitars = []
guitars = []


class Guitar:
    def __init__(self, name, year, cost):
        self.name = name
        self.year = year
        self.cost = cost

    def is_vintage(self):
        return self.year <= 1920 or (self.year <= 2021 and (2021 - self.year) >= 50)


def main():
    in_file = open('guitars.csv', 'r', newline='')
    in_file.readline()
    guitar_data = csv.reader(in_file)
    for row in guitar_data:
        guitars.append(row)
    in_file.close()

    for guitar in guitars:
        class_guitars.append(Guitar(guitar[0], int(guitar[1]), float(guitar[2])))

    class_guitars.sort()

    for i, guitar in enumerate(class_guitars, 1):
        vintage_string = "(vintage)" if guitar.is_vintage() else ""
        print(f"Guitar {i}: {guitar.name:>20} ({guitar.year}), worth ${guitar.cost:10,.2f} {vintage_string}")


if __name__ == '__main__':
    main()
