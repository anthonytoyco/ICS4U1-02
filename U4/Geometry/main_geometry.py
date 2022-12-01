import geometry as geo

# FUNCTIONS


def display_results(option, figure_vol, figure_sa):
    figure = ""
    if option == 1:
        figure = "rectangular prism"
    elif option == 2:
        figure = "cylinder"
    print(
        f"\nThis {figure} has a volume of {round(figure_vol, 2):,} units³"
        f" and a surface area of {round(figure_sa, 2):,} units²"
    )


def cylinder_calcs():
    while True:
        try:
            radius = float(input("\nEnter the cylinder's radius: "))
            height = float(input("\nEnter the cylinder's height: "))
            if (radius >= 1) and (height >= 1):
                break
            else:
                print("\n***ERROR: Please enter positive decimal numbers!***")
        except ValueError:
            print("\n***ERROR: Please enter positive decimal numbers!***")
    return geo.volume_cylinder(radius, height), geo.surface_area_cylinder(
        radius, height
    )


def rect_prism_calcs():
    while True:
        try:
            length = float(input("\nEnter the rectangular prism's length: "))
            width = float(input("\nEnter the rectangular prism's width: "))
            height = float(input("\nEnter the rectangular prism's height: "))
            if (length >= 1) and (width >= 1) and (height >= 1):
                break
            else:
                print("\n***ERROR: Please enter positive decimal numbers!***")
        except ValueError:
            print("\n***ERROR: Please enter positive decimal numbers!***")
    return geo.volume_rectangular_prism(
        length, width, height
    ), geo.surface_area_rectangular_prism(length, width, height)


def get_option():
    while True:
        try:
            answer = int(
                input(
                    "\nPlease select a figure from the options below:"
                    "\n\t- Rectangular Prism [Enter '1']"
                    "\n\t- Cylinder [Enter '2']"
                    "\n\nEnter your selected option: "
                )
            )
            if answer in [1, 2]:
                return answer
            else:
                print("\n***ERROR: Please enter a valid option!***")
        except ValueError:
            print("\n***ERROR: Please enter a valid option!***")


def main():
    run_again = "Y"
    while run_again == "Y":

        user_option = get_option()

        if user_option == 1:
            rect_prism_vol, rect_prism_sa = rect_prism_calcs()
            display_results(user_option, rect_prism_vol, rect_prism_sa)
        elif user_option == 2:
            cylinder_vol, cylinder_sa = cylinder_calcs()
            display_results(user_option, cylinder_vol, cylinder_sa)

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
