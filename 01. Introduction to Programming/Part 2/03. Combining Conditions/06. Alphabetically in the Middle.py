# Please write a program which asks the user for three letters. The program should then print out whichever of the three letters would be in the middle if the letters were in alphabetical order.

# User enters numbers
letter_1 = input("Enter a letter")
letter_2 = input("Enter a second letter")
letter_3 = input("Enter a third letter")

# Letter 1 is the middle letter
if letter_1 > letter_2 and letter_1 < letter_3 or letter_1 < letter_2 and letter_1 > letter_3:
    print(f"The letter in the middle is {letter_1}")
# Letter 2 is the middle letter
elif letter_2 > letter_1 and letter_2 < letter_3 or letter_2 < letter_1 and letter_2 > letter_3:
    print(f"The letter in the middle is {letter_2}")
# Letter 3 is the middle letter
else:
    print(f"The letter in the middle is {letter_3}")


# Alternate Solution
"""
# Read three letters 
a = input("1st letter: ")
b = input("2nd letter: ")
c = input("3rd letter: ")

# Decide who is largest first, then choose the middle from the other two
if a > b and a > c:            # a is the largest
    middle = b if b > c else c
elif b > a and b > c:          # b is the largest
    middle = a if a > c else c
else:                          	# c is the largest 
    middle = a if a > b else b

print(f"The letter in the middle is {middle}")
"""
