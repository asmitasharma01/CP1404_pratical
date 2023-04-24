"""
CP1404 Write a program that stores users' emails (unique keys)
and names (values) in a dictionary
"""


def extract_name(email):
    """Extracts the name from an email address."""
    username = email.split('@')[0]
    name_parts = username.split('.')
    name = ' '.join(part.title() for part in name_parts)
    return name


# Ask for user input until a blank email is entered
users = {}
while True:
    email = input("Enter email (blank to end): ")
    if email == "":
        break

    name = extract_name(email)
    print("Is this name correct? (Y/n):", name)
    response = input().lower()
    if response != "" and response != "y":
        name = input("Enter name: ")
    users[email] = name

# Print out the dictionary contents
for email, name in users.items():
    print(f"{email}: {name}")
