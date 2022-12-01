# FUNCTIONS


def ascii(number):
    try:
        if 33 <= number <= 126:
            print(
                f"\nThe Decimal integer {number} when converted to "
                f"ASCII is {chr(number)}"
            )
        elif 0 <= number <= 32 or number == 127:
            print(
                f"\nThe converted ASCII value of {number} "
                f"can not be displayed!"
            )
        else:
            print("\n***ERROR: This number can not be converted to ASCII!***")
    except ValueError:
        print("\n***ERROR: This number can not be converted to ASCII!***")


def hexadecimal(number):
    print(
        f"\nThe Decimal integer {number} when converted to "
        f"Hexadecimal is {hex(number)}"
    )


def binary(number):
    print(
        f"\nThe Decimal integer {number} when converted to "
        f"Binary is {bin(number)}"
    )


def main():
    run_again = "Y"
    while run_again == "Y":
        print(
            "\nSelect an option:"
            "\n\t1. Convert Decimal to ASCII"
            "\n\t2. Convert Decimal to Hexadecimal"
            "\n\t3. Convert Decimal to Binary"
            "\n\t4. Exit Program"
        )

        while True:
            try:
                user_choice = int(input("\nEnter an option: "))
                if user_choice in [1, 2, 3, 4]:
                    break
                else:
                    print("\n***ERROR: Please enter a 1, 2, 3, or 4!***")
            except ValueError:
                print("\n***ERROR: Please enter a valid option! (1 - 4)***")
        if user_choice == 4:
            break

        while True:
            try:
                user_decimal = int(
                    input(
                        "\nEnter a Decimal integer you would like to convert: "
                    )
                )
                break
            except ValueError:
                print("\n***ERROR: Please enter a valid Decimal integer!***")

        if user_choice == 1:
            ascii(user_decimal)
        elif user_choice == 2:
            hexadecimal(user_decimal)
        elif user_choice == 3:
            binary(user_decimal)

        while True:
            try:
                run_again = str(
                    input("\nWould you like to repeat the program? [Y/n]: ")
                )
                if run_again in ["Y", "n"]:
                    break
                else:
                    print("\n***ERROR: Please enter a valid option! [Y/n]***")
            except ValueError:
                print("\n***ERROR: Please enter a valid option! [Y/n]***")


# MAIN PROGRAM


if __name__ == "__main__":
    main()
