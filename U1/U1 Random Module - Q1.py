import random as r

dice_a_1 = r.randint(2, 12)
print(f"\nResult of one dice, generating a number from 2-12: {dice_a_1}")

# PART B
dice_b_1 = r.randint(1, 6)
dice_b_2 = r.randint(1, 6)
print(
    f"Result of the sum of two dice, generating a number from 1-6 each: "
    f"{dice_b_1} + {dice_b_2} = {dice_b_1 + dice_b_2}\n"
)
