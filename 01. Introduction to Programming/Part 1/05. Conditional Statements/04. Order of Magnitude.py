# Please write a program which asks the user for an integer number. The program should then print out the magnitude of the number.

# User input
num = int(input("Please type in a number:"))

# Code to run, dependant on number given
if num <1000:
    print("This number is smaller than 1000")
if num <100:
    print("This number is smaller than 100")
if num <10:
    print("This number is smaller than 10")

# Always print this, regardless of user input
print ("Thank you!")
