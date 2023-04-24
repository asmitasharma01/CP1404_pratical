"""
Write a program that allows you to look up hexadecimal colour code like those
"""

COLORS = {
    "BISTRE": "#3d2b1f",
    "BLACK": "#000000",
    "BROWN": "#a52a2a",
    "BLUE": "#0000ff",
    "GRAY": "#808080",
    "GREEN": "#008000",
    "NAVY": "#000080",
    "ORANGE": "#ffa500",
    "PURPLE": "#800080",
    "RED": "#ff0000",
    "WHITE": "#ffffff",
    "YELLOW": "#ffff00",
}

while True:
    color_name = input("Enter a color name to get its hexadecimal code (or press enter to quit): ")
    if color_name.strip() == "":
        break
    color_name = color_name.upper()
    if color_name in COLORS:
        print(f"The hexadecimal code for {color_name} is {COLORS[color_name]}.")
    else:
        print(f"Sorry, {color_name} is not a valid color name.")
