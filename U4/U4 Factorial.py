# FUNCTIONS


def output_result(number, total):
    print(f"\nThe factorial of {number} is {total:,}")


def factorial(number):
    total = 1
    for i in range(1, number + 1):
        total *= i
    return total


def get_n():
    while True:
        try:
            number = int(input("\nEnter a positive integer: "))
            if number >= 1:
                return number
            else:
                print("\n***ERROR: Please enter a valid number!***")
        except ValueError:
            print("\n***ERROR: Please enter a valid number!***")


def main():
    run_again = "Y"
    while run_again == "Y":

        user_number = get_n()

        factorial_result = factorial(user_number)

        output_result(user_number, factorial_result)

        while True:
            try:
                run_again = str(
                    input("\nWould you like to repeat the program? [Y/n]: ")
                )
                if run_again in ["Y", "n"]:
                    if run_again == "n":
                        print("\nThanks for using this program!\n")
                    break
                else:
                    print("\n***ERROR: Please enter a valid option! [Y/n]***")
            except ValueError:
                print("\n***ERROR: Please enter a valid option! [Y/n]***")


# MAIN PROGRAM


if __name__ == "__main__":
    main()
