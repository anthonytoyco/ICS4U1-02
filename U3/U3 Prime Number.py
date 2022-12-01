# FUNCTIONS


def prime_check(number):
    for i in range(2, number):
        if (number % i) == 0:
            return False
    return True


def collect_primes(integer):
    primes = []
    for num in range(2, integer + 1):
        if prime_check(num):
            primes.append(num)
    return primes


def main():
    run_again = "Y"
    while run_again == "Y":
        while True:
            try:
                user_integer = int(input("\nEnter an positive integer: "))
                if user_integer >= 1:
                    break
                else:
                    print("\n***ERROR: Please enter a valid number!***")
            except ValueError:
                print("\n***ERROR: Please enter a valid number!***")

        primes = collect_primes(user_integer)

        print(
            f"\nBetween the numbers 1 to {user_integer}, "
            f"there are {len(primes)} prime number(s):\n{primes}"
        )

        while True:
            try:
                run_again = str(
                    input("\nWould you like to repeat the program? [Y/n]: ")
                )
                if run_again in ["Y", "n"]:
                    primes.clear()
                    break
                else:
                    print("\n***ERROR: Please enter a valid option! [Y/n]***")
            except ValueError:
                print("\n***ERROR: Please enter a valid option! [Y/n]***")


# MAIN PROGRAM


if __name__ == "__main__":
    main()
