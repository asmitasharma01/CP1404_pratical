"""
Convert temperatures between Celsius and Fahrenheit.
"""
MENU = """C - Convert Celsius to Fahrenheit
F - Convert Fahrenheit to Celsius 
Q - Quit """


def main():
    """Convert temperature between Celsius and Fahrenheit."""
    print(MENU)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "C":
            Celsius = float(input("Celsius: "))
            fahrenheit = convert_to_fahrenheit(Celsius)
            print("Result: {:.2f} F".format(fahrenheit))
        elif choice == "F":
            fahrenheit = float(input("Fahrenheit: "))
            Celsius = convert_to_celsius(fahrenheit)
