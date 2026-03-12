"""
Create a program that asks the user to enter a password. The program should keep asking until the user enters a password
that meets the following criteria:

1.	at least 8 characters long,
2.	contains both uppercase and lowercase letters,
3.	and includes at least one number

"""


def is_valid_password(password):
    # Check for minimum length
    if len(password) < 8:
        return False

    # Flags for required character types
    has_upper = any(c.isupper() for c in password)
    has_lower = any(c.islower() for c in password)
    has_digit = any(c.isdigit() for c in password)

    # Return True only if all conditions are met
    return has_upper and has_lower and has_digit


# Main loop
password_accepted = False
while password_accepted is False:
    password = input("Enter a password: ")
    if is_valid_password(password):
        print("Password accepted.")
        password_accepted = True
    else:
        print("Invalid password.\nMust be at least 8 characters long,"
              "contain both uppercase and lowercase letters, and include at least one number.")
