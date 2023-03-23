def get_valid_score():
    """
    Gets a valid score from the user.
    """
    while True:
        try:
            score = int(input("Enter a score (0-100 inclusive): "))
            if 0 <= score <= 100:
                return score
            else:
                print("Invalid score. Please enter a score between 0 and 100 inclusive.")
        except ValueError:
            print("Invalid input. Please enter a valid integer.")


def print_result(score):
    """
    Prints the result corresponding to the given score.
    """
    if score >= 90:
        print("A")
    elif score >= 80:
        print("B")
    elif score >= 70:
        print("C")
    elif score >= 60:
        print("D")
    else:
        print("F")


def show_stars(score):
    """
    Prints stars corresponding to the given score.
    """
    print("*" * score)


def main():
    score = get_valid_score()
    while True:
        print("Menu:")
        print("(G)et a valid score")
        print("(P)rint result")
        print("(S)how stars")
        print("(Q)uit")
        choice = input("Enter your choice: ").upper()
        if choice == "G":
            score = get_valid_score()
        elif choice == "P":
            print_result(score)
        elif choice == "S":
            show_stars(score)
        elif choice == "Q":
            print("Farewell!")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()



































