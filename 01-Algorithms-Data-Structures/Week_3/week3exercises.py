"""
Exercise 1:
For this exercise, you could reuse some of the code you wrote in week 2 for exercise 1.
A fruit company sells bananas for £3.00 a kilogram plus £4.99 per order for postage and packaging. If an order is over
£50.00, the P&P is reduced by £1.50. Write a function order_price(quantity) that takes an int parameter quantity
representing the number of kilo of bananas for the order, and returns the cost of the order in pence (as an int).
"""


def order_price(quantity):
    # Constants
    PRICE_PER_KG = 3.00  # in pounds
    P_AND_P = 4.99  # standard postage and packaging in pounds
    DISCOUNT_THRESHOLD = 50.00  # threshold for P&P discount
    DISCOUNT_AMOUNT = 1.50  # discount on P&P for orders over threshold

    # Get input from the user

    if not isinstance(quantity, int):
        raise ValueError("The quantity must be an integer")

    # Calculate cost of bananas
    banana_cost = quantity * PRICE_PER_KG

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
    return total_cost_pence


"""
Exercise 2:
Again, you could use some of the code you have written in week 2 for exercise 2.
Write a function maximum_heart_rate(age) that takes the age of the person as parameter (an int) and returns the maximum
heart rate for that person (as an int). 
"""


# Calculate maximum heart rate
def maximum_heart_rate(age):
    if not isinstance(age, int):
        raise ValueError("The age must be an integer")
    else:
        max_heart_rate = 208 - 0.7 * age
        return max_heart_rate


def training_zone(age, rate):
    if not isinstance(rate, int):
        raise ValueError("The rate must be an integer")
    # Determine training zone
    if rate >= 0.9 * maximum_heart_rate(age):
        zone = "Interval training"
    elif rate >= 0.7 * maximum_heart_rate(age):
        zone = "Threshold training"
    elif rate >= 0.5 * maximum_heart_rate(age):
        zone = "Aerobic training"
    else:
        zone = "Couch potato"

    return zone


"""
Exercise 3
Create a function that asks the user to enter a password that takes the following parameters in that order:

1.	password: a password as a string
2.	has_upper: a Boolean. If True the password must contains at least one uppercase character  
3.	has_lower: a Boolean. If True the password must contains at least one lowercase character 
4.	has_numeric: a Boolean. If True the password must contains at least one numeric character 

The function returns True if the password meets the following criteria:
 
1.	at least min_length characters long, 
2.	contains at least one uppercase character if has_upper is True
3.	contains at least one lowercase character if has_lower is True 
4.	contains at least one numeric character if has_numeric is True
5.	Does not contain any special characters (that is non-alphanumeric like punctuation)

"""


def is_valid_password(password,
                      min_length=8,
                      has_upper=True,
                      has_lower=True,
                      has_numeric=True):
    # Check for password greater than minimum length
    if len(password) < min_length:
        return False

    # Check for non-alphanumeric characters
    if not password.isalnum():
        raise ValueError("The password must contain only alphanumeric values")

    # Flags for required character types
    if not password.isalnum():
        return False  # Contains special characters

    if has_upper and not any(char.isupper() for char in password):
        return False

    if has_lower and not any(char.islower() for char in password):
        return False

    if has_numeric and not any(char.isdigit() for char in password):
        return False

    return True


"""
Exercise 4

Write a function sum_digits(number) to calculate and return the sum of the digits of a given whole number
(an int NOT a string) given as a parameter. 
"""


def sum_digits(number):
    total_sum = 0
    for n in str(number):
        total_sum += int(n)
    return total_sum


"""
Exercise 5

Write a function pairwise_digits(number_a, number_b) that takes two whole numbers represented by strings (not int) as
parameters and returns a binary string where a character 1 is used if the digits at the same index are the same, a 0
otherwise. If the two strings have different lengths, the output should be padded with 0s on the right-hand side to
match the length of the longest string.
"""


def pairwise_digits(number_a, number_b):
    # Check which number is longer

    length_a = len(number_a)
    length_b = len(number_b)
    index_a = length_a - 1
    index_b = length_b - 1
    result = ""

    if length_a == length_b:

        for ind, c in enumerate(number_a):
            if not c == number_b[ind]:
                result += "0"
            else:
                result += "1"

        return result

    if length_a > length_b:
        for ind, c in enumerate(number_b):
            if not c == number_a[ind]:
                result += "0"
            else:
                result += "1"
        if len(result) < length_a:
            result += "0" * (length_a - len(result))
    else:
        for ind, c in enumerate(number_a):
            if not c == number_b[ind]:
                result += "0"
            else:
                result += "1"
        if len(result) < length_b:
            result += "0" * (length_b - len(result))

    return result



