"""
MENU = C - Convert Celsius to Fahrenheit
F - Covert Fahrenheit to Celsius
Q - Quit
"""


# Python program to convert given temperature from Celsius to Fahrenheit and vice versa.

# function to convert temperature given in Celsius to Fahrenheit which takes Celsius temperature as argument
def CelsiusToFahrenheit(celsius):
    fahrenheit = (celsius * 1.8) + 32
    return fahrenheit


# function to convert temperature given in Fahrenheit to Celsius which takes Fahrenheit temperature as argument
def FahrenheitToCelsius(fahrenheit):
    celsius = (fahrenheit - 32) / 1.8
    return celsius


# main function
def main():
    print("Enter your choice:\n1.Celsius to Fahrenheit\n2.Fahrenheit to Celsius")
    choice = int(input())
    if choice == 1:
        Celsius = float(input("Enter temperature in Celsius:"))
        print("Temperature in fahrenheit is:", CelsiusToFahrenheit(Celsius))
    else:
        fahrenheit = float(input("Enter temperature in Fahrenheit:"))
        print("Temperature in Celsius is:", FahrenheitToCelsius(fahrenheit))


# calling main function
if __name__ == "__main__":
    main()
