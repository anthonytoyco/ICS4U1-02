from math import sqrt
from random import randint

# FUNCTIONS


def exception_check(user_input, average_of_list, standard_deviation):
    if (
        (average_of_list - standard_deviation)
        < user_input
        < (average_of_list + standard_deviation)
    ):
        print(
            f"\nWith an average of {round(average_of_list, 4)} "
            f"and a standard deviation of {round(standard_deviation, 4)},"
            f"\nthe value {round(user_input, 4)} is not exceptional"
        )
    else:
        print(
            f"\nWith an average of {round(average_of_list, 4)} "
            f"and a standard deviation of {round(standard_deviation, 4)}, "
            f"\nthe value {round(user_input, 4)} is exceptional"
        )


def get_user_input():
    while True:
        try:
            user_input = int(input("\nEnter a positive integer: "))
            if user_input >= 1:
                return user_input
            else:
                print("\n***ERROR: Please enter a valid number!***")
        except ValueError:
            print("\n***ERROR: Please enter a valid number!***")


def get_standard_deviation(int_list):
    u = 0
    for i in int_list:
        u += i
    u = u / len(int_list)

    square_differences = []
    for i in int_list:
        square_differences.append((i - u) ** 2)

    v = 0
    for i in square_differences:
        v += i
    v = v / len(square_differences)

    v = sqrt(v)
    return u, v


# MAIN PROGRAM


def main():
    run_again = "y"
    while run_again == "y":

        list_of_ints = []
        for i in range(1, 151):
            list_of_ints.append(randint(25, 75))

        average_of_list, standard_deviation = get_standard_deviation(
            list_of_ints
        )

        exception_check(get_user_input(), average_of_list, standard_deviation)

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
