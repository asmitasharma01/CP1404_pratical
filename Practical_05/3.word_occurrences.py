"""
Write a program to count the occurrences of words in a string.
The program should ask the user for a string, then print the
counts of how many of each word are in the string.
Estimate: 20 minutes
Actual:   35 minutes
"""


def count_words():
    # Get the input string from the user
    text = input("Enter a string: ")

    # Split the string into words
    words = text.split()

    # Create an empty dictionary to store word counts
    counts = {}

    # Count the occurrences of each word
    for word in words:
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1

    # Find the length of the longest word
    max_len = max(len(word) for word in counts.keys())

    # Print the results in a sorted and aligned format
    for word, count in sorted(counts.items()):
        print(f"{word:{max_len}} : {count}")


# Call the function
count_words()
