"""Create a program that converts the weight of a person from stones and pounds to kilograms.
The program requests two integer inputs from the user, one for the stones and one for the pounds,
and prints the weight of the person in kilograms.
"""

# Conversion factors
STONE_TO_POUNDS = 14
POUND_TO_KG = 0.45359237

# Get input from the user
stones = int(input("Enter weight in stones: "))
pounds = int(input("Enter additional weight in pounds: "))

# Convert total weight to pounds
total_pounds = stones * STONE_TO_POUNDS + pounds

# Convert pounds to kilograms
kilograms = total_pounds * POUND_TO_KG

# Print the result
print(f"The weight in kilograms is: {kilograms:.2f} kg")