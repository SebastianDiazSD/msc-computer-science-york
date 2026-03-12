"""
Write a script that takes the age (int) and rate (the heart rate as an int) from the user and prints a description of a
person's training zone based on his or her age and training heart rate, rate. The zone is determined by comparing rate
with the person's maximum heart rate m:

Interval range      |   Training Zone
rate≥0.9 m          |   Interval training
0.7 m≤rate<0.9 m    |   Threshold training
0.5 m≤rate<0.7 m    |   Aerobic training
rate<0.5 m          |   Couch potato

 The maximum heart rate m in beats per minute is given by the formula:
m=208-0.7×age

"""


# Get inputs from user
age = int(input("Enter your age: "))
rate = int(input("Enter your heart rate (in bpm): "))

# Calculate maximum heart rate
max_heart_rate = 208 - 0.7 * age

# Determine training zone
if rate >= 0.9 * max_heart_rate:
    zone = "Interval training"
elif rate >= 0.7 * max_heart_rate:
    zone = "Threshold training"
elif rate >= 0.5 * max_heart_rate:
    zone = "Aerobic training"
else:
    zone = "Couch potato"

# Print the result
print(f"Your training zone is: {zone}")
