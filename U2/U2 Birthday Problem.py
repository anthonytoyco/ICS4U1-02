# FUNCTIONS #


def prob_formula(people):
    prob_formula_ans = 365 / 365

    for i in range(1, people + 1):
        prob_formula_ans *= ((365 - i) + 1) / 365
    return prob_formula_ans


# MAIN PROGRAM #


while True:
    try:
        num_of_people = int(input("\nHow many people are in the room?: "))
        if num_of_people <= 0:
            print("\n*** ERROR ****\nPlease enter a positive integer!")
        else:
            break
    except ValueError:
        print("\n*** ERROR ****\nPlease enter a positive integer!")

prob_percentage = round((1 - prob_formula(num_of_people)) * 100, 2)

print(
    f"\nIn this room of {num_of_people} people, the probability of at least "
    f"two people sharing the same birthday is:\n{prob_percentage}%\n"
)
