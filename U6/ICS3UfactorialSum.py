"""
Filename: ICS3UfactorialSum.py
Author: Anthony Toyco
Date: January 12, 2023
Description: A program that calculates the sum of all factorials
entered by the user.
"""

# FUNCTIONS


def factorial(numbers):
    sums = 0
    for number in numbers:
        total = 1
        for i in range(number, 0, -1):
            total *= i
        sums += total
    return sums


def main():
    run_again = "y"
    while run_again == "y":
        factorials = []
        while True:
            try:
                number = int(
                    input(
                        "\nEnter a number OR '0' to calculate factorial sum: "
                    )
                )
                if number == 0:
                    if len(factorials) == 0:
                        factorials.append(1)
                    break
                if number > 0:
                    factorials.append(number)
                else:
                    print("\n***ERROR: Please enter a positive number!***")
            except ValueError:
                print("\n***ERROR: Please enter a positive number!***")

        factorial_sum = factorial(factorials)

        print(f"\nThe sum of the factorials is {factorial_sum}")

        while True:
            try:
                run_again = str(
                    input("\nWould you like to repeat the program? [y/N]: ")
                )
                if run_again in ["y", "N"]:
                    if run_again == "N":
                        print("\nThanks for using this program!\n")
                    break
                else:
                    print("\n***ERROR: Please enter a valid option! [y/N]***")
            except ValueError:
                print("\n***ERROR: Please enter a valid option! [y/N]***")


# MAIN PROGRAM


if __name__ == "__main__":
    main()
