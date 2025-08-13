# Please write a program which asks the user for two numbers and an operation. If the operation is add, multiply or subtract, the program should calculate and print out the result of the operation with the given numbers. If the user types in anything else, the program should print out nothing.

# User inputs two numbers and an operation
num1 = int(input("Enter a number"))
num2 = int(input("Enter a second number"))
operation = input("Enter operation").lower()

# What code to run when an operation is chosen
if operation == "add":
    print(f"{num1} + {num2} = {num1 + num2}")
if operation == "multiply":
    print(f"{num1} * {num2} = {num1 * num2}")
if operation == "subtract":
    print(f"{num1} - {num2} = {num1 - num2}")