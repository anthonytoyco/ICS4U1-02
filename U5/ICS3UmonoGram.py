# FUNCTIONS


def get_monogram(name):
    monogram = ""
    monogram = name[0][0].lower() + name[2][0].upper() + name[1][0].lower()
    return monogram


def get_name():
    while True:
        try:
            user_name = str(
                input(
                    "\nEnter your full name in the format: first middle last"
                    "\nEnter a empty name to quit the program"
                    "\nYour name: "
                )
            )
            if user_name == "":
                return user_name
            elif all((user_name.isspace() for user_name in user_name)):
                print("\n***ERROR: Please enter a name!***")
            elif all(
                user_name.isalpha() or user_name.isspace()
                for user_name in user_name
            ) and (len(user_name.split()) == 3):
                return user_name
            else:
                raise ValueError
        except ValueError:
            print("\n***ERROR: Please enter a valid name!***")


def main():
    run_again = "y"
    while run_again == "y":
        name = get_name()
        name_in_list = name.split()
        if name != "":
            print(
                f"For the name "
                f"{name_in_list[0]} {name_in_list[1]} {name_in_list[2]},"
                f" your monogram is {get_monogram(name_in_list)}"
            )
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
                        print(
                            "\n***ERROR: Please enter a valid option! [y/N]***"
                        )
                except ValueError:
                    print("\n***ERROR: Please enter a valid option! [y/N]***")
        else:
            print("\nThanks for using this program!\n")
            run_again = "N"


# MAIN PROGRAM


if __name__ == "__main__":
    main()
