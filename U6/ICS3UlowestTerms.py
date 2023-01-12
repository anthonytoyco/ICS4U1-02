"""
Filename: ICS3UlowestTerms.py
Author: Anthony Toyco
Date: January 12, 2023
Description: A program that converts a fraction to its lowest terms.
"""

# FUNCTIONS


def greatest_common_divisor(numerator, denominator):
    numer = numerator
    denom = denominator
    while denominator:
        numerator, denominator = denominator, numerator % denominator
    lowest = numerator
    numerator = numer // lowest
    denominator = denom // lowest
    return numerator, denominator


def main():
    run_again = "y"
    while run_again == "y":
        while True:
            try:
                fraction = str(input("\nEnter a fraction in the form 'n/d': "))
                if ("/" in fraction) and (fraction.count("/") == 1):
                    fraction = fraction.split("/")
                    numerator = int(fraction[0])
                    denominator = int(fraction[1])
                    if numerator != 0 or denominator != 0:
                        break
                    else:
                        print("\n***ERROR: Please enter a valid fraction!***")
                else:
                    print("\n***ERROR: Please enter a valid fraction!***")
            except ValueError:
                print("\n***ERROR: Please enter a valid fraction!***")

        numerator, denominator = greatest_common_divisor(numerator, denominator)

        print(f"\nThe lowest terms are {numerator}/{denominator}")

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
