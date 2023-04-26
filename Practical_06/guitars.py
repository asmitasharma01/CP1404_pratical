"""
Estimated time : 30 minutes
Actual time : 1 hour 30 minutes
"""
import guitar as guitar

from Practical_06.guitar import guitar

guitars = []


def main():
    print("My guitars!")
    name = input("Name: ")
    while name != "":
        year = int(input("Year: "))
        cost = float(input("Cost: $"))
        guitars.append(guitar(name, year, cost))
        print(f"{guitar(name, year, cost)} added.", end="\n\n")
        name = input("Name")
    print("These are my guitars:")
    guitars.append(guitar("Gibson L-5 CES", 1922, 16035.40))
    guitars.append(guitar("Line 6 JTV-59", 2010, 1512.9))
    guitars.sort()
    for i, guitar in enumerate(guitars,1):
        vintage_string = "(vintage)" if guitar.is_vintage() else ""
        print(f"guitar {i}: {guitar.name:>20} ({guitar.year}), worth ${guitar.cost:10,.2f} {vintage_string}")