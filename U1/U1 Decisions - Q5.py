import math

while True:
    coeff_a = 0.0
    coeff_b = 0.0
    coeff_c = 0.0
    try:
        coeff_a = float(input("\nEnter the value for the 'a' coefficient: "))
        coeff_b = float(input("Enter the value for the 'b' coefficient: "))
        coeff_c = float(input("Enter the value for the 'c' coefficient: "))
        if coeff_a == 0:
            print("\nERROR: Please enter a valid integer or decimal number.")
        else:
            break
    except ValueError:
        print("\nERROR: Please enter a valid integer or decimal number.")

discriminant = (coeff_b**2) - 4 * (coeff_a * coeff_c)
print(f"\nThe discriminant is {int(discriminant)}")

if discriminant < 0:
    print(
        "\nThere are no real roots for this quadratic equation. "
        "There are two complex roots instead."
    )
else:
    quadratic_positive = (
        -1 * (coeff_b) + math.sqrt((coeff_b**2) - 4 * (coeff_a * coeff_c))
    ) / (2 * coeff_a)
    quadratic_negative = (
        -1 * (coeff_b) - math.sqrt((coeff_b**2) - 4 * (coeff_a * coeff_c))
    ) / (2 * coeff_a)
    if discriminant > 0:
        print(
            f"\nThere are two roots for this quadratic equation: "
            f"\nx = {round(quadratic_positive, 3)}"
            f"\nx = {round(quadratic_negative, 3)}"
        )
    elif discriminant == 0:
        print(
            f"\nThere are two identical roots for this quadratic equation: "
            f"\nx = {round(quadratic_positive, 3)}"
        )
