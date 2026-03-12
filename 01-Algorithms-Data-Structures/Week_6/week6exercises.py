# Exercise 1
# We want to create a function sum_from_file(filename) that calculate the sum of all int contained
# in the text file filename. The format of the text file is as follow, a series of int separated by
# a space spanning several lines as shown below. In the example below the returned value should be 100.
# 1 30 4 5
# 8 12 19 1
# 5 5 10
#
# 1.	It is sometime useful to decompose the problem into smaller problem. In this case it would be
# useful to have a function sum_numbers(a_string) that calculates and returns the sum of all numbers
# contained in the string a_string. The format of the string is a series of int separated by a space.
#
# For example:
# >>> sum_numbers('1 30 4 5')
# 40
#
# It could be useful to remember /check some the methods already existing for str object.
# 2.	The function should raise a ValueError when the format of the file is not as described.
# 3.	The function should return None if the file passed in parameters does not exist

def sum_numbers(a_string):
    parts = a_string.strip().split()  # Split the string into parts
    total = 0
    for part in parts:
        if not part.isdigit() and not (part.startswith('-') and part[1:].isdigit()):
            # If the part is not a valid integer, raise an error
            raise ValueError("Invalid number found in the string.")
        total += int(part)
    return total


# This function reads a file and returns the sum of all numbers in it
def sum_from_file(filename):
    try:
        total = 0
        with open(filename, 'r') as file:
            for line in file:
                line_sum = sum_numbers(line)  # Use helper function to sum each line
                total += line_sum
        return total
    except FileNotFoundError:
        # If the file doesn't exist, return None
        return None
    except ValueError:
        # If the file contains bad formatting, raise an error
        raise ValueError("The file has an invalid format (only space-separated integers are allowed).")


# Exercise 2:
# The aim of this exercise is to compute the score of an athlete in a given track event. We need to convert
# a time in seconds into points. The formula is:
#
# points=a(b-time)^c
#
# Where time is the time in seconds of the athlete for that event. a, b and c are parameters that vary depending
# on the event (see Table 1). The value of points must be rounded down to a whole number after applying the
# respective formula (e.g. 499.999 points becomes 499). If the value of points is less than 0, then 0 should
# be returned instead.
#
# Table 1: Constants a, b and c for each event
# Women's events	a	b	c
# 200 m	4.99087	42.5   	1.81
# 800 m	0.11193	254.0   	1.88
# 110 m	9.23076	26.7   	1.835
#
# Write a function track_points(time, eventParameters) which takes a float parameter  time representing the
# athlete's time in seconds, and a tuple containing the event's parameters (a, b, c) in that order. The method
# returns an int representing the points scored for that event using Equation provided earlier.
#
# The method raises a ValueError if eventParameters does not have exactly 3 values.
# For example:
# 	200 metres time of 22.83 seconds corresponds to 1,096 points
# 	110 metres hurdles time of 12.54 seconds corresponds to 1,195 points
# 	800 metres time of 128.65 seconds (i.e. 02:08.65) corresponds to 984 points

def track_points(time, eventParameters):
    if len(eventParameters) != 3:
        raise ValueError("eventParameters must contain exactly 3 values: (a, b, c)")
    elif time == 0:
        return 0
    else:
        points = int(eventParameters[0] * ((eventParameters[1] - time) ** eventParameters[2]))
        return points

# Exercise 3:
# Write a function rasterise(list_1D, width) that transforms a 1D list passed as parameter into a 2D list,
# where each sub-list have width elements. If the length of the 1D list is not a multiple of width, the function
# must raise a BufferError with an appropriate error message. If width is less than 1, the function must raise a
# ValueError with an appropriate error message.
#
# For example:
# >>> rasterise([1,2,3,4,5,6,7,8],4)
# [[1,2,3,4],[5,6,7,8]]
# >>> rasterise([1,2,3,4,5,6,7,8],2)
# [[1,2],[3,4],[5,6],[7,8]]
# >>> rasterise([1,2,3,4,5,6,7,8],3)
# BufferError: invalid width!

def rasterise(list_1D, width):
    # Check if the list can be evenly divided
    if len(list_1D)%width!=0:
        raise BufferError("invalid width!List cannot be evenly divided.")
    # Check if the width is less than 1
    elif width<1:
        raise ValueError("Width must be at least 1.")

    total_list=[]
    sub_list=[]

    for element in list_1D:
        sub_list.append(element)
        if len(sub_list)==width:
            total_list.append(sub_list)
            sub_list = []

    print(total_list)
