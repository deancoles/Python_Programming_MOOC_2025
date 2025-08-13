# Please write a program which asks the user for an integer number. If the number is less than zero, the program should print out the number multiplied by -1. Otherwise the program prints out the number as is.

# User inputs a number
num = int(input("Please type in a number:"))

# If number is less than zero, multiply by one, otherwise print the given number
if num <0:
    print(f"The absolute value of this number is {num * -1}")
else:
    print(f"The absolute value of this number is {num}")
