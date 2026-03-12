"""
A fruit company sells bananas for £3.00 a kilogram plus £4.99 per order for postage and packaging.
If an order is over £50.00, the P&P is reduced by £1.50.
Write a script that requests the user to enter the number of kilo of bananas and print the cost of the order in pence.
"""

# Constants
PRICE_PER_KG = 3.00           # in pounds
P_AND_P = 4.99                # standard postage and packaging in pounds
DISCOUNT_THRESHOLD = 50.00    # threshold for P&P discount
DISCOUNT_AMOUNT = 1.50        # discount on P&P for orders over threshold

# Get input from the user
kilos = float(input("Enter the number of kilograms of bananas: "))

# Calculate cost of bananas
banana_cost = kilos * PRICE_PER_KG

# Determine postage and packaging cost
if banana_cost > DISCOUNT_THRESHOLD:
    postage = P_AND_P - DISCOUNT_AMOUNT
else:
    postage = P_AND_P

# Total cost in pounds
total_cost_pounds = banana_cost + postage

# Convert to pence
total_cost_pence = round(total_cost_pounds * 100)

# Print the result
print(f"The total cost of the order is: {total_cost_pence} pence")