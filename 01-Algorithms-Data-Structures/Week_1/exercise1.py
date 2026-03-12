"""Let’s try to create a small program that computes a bill for a cake shop. You would like to get
the number of cakes, the price of a single cake and then print the total price of the bill. """

number_cakes = int(input("Enter the number of cake(s) zou want to buy: "))
cake_price = 2.5
bill = cake_price * number_cakes
print("The price of", number_cakes, "cake(s) is", bill, "pounds")
