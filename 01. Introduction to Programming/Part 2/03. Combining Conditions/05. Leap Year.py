# Please write a program which asks the user for a year, and then prints out whether that year is a leap year or not.

# Ask for a year
year = int(input("Please type in a year: "))

# # First check: Is the year divisible by 4? If not, it's not a leap year.
if year % 4 == 0:
    # If divisible by 4, now check if it's also divisible by 100.
    if year % 100 == 0:
        # If divisible by 100, check if it is also divisible by 400.
        if year % 400 == 0:
            print("That year is a leap year.")
        else:
            print("That year is not a leap year.")
    else:
        # Divisible by 4 but not a century year
        print("That year is a leap year.")
else:
     # Not divisible by 4 
    print("That year is not a leap year.")


# Alternate Solution
"""

# Ask the user for a year and convert to an integer
year = int(input("Please type in a year: "))
 
# Start by assuming it's NOT a leap year
leap_year = False

# First check: Is it divisible by 100?
if year % 100 == 0:
	# If divisible by 100, it must also be divisible by 400 to be a leap year
    if year % 400 == 0:
        leap_year = True
# If not divisible by 100, check if it's divisible by 4
elif year % 4 == 0:
    leap_year = True

# Finally, print result based on leap_year flag
if leap_year:
    print("That year is a leap year.")
else:
    print("That year is not a leap year.")

"""
