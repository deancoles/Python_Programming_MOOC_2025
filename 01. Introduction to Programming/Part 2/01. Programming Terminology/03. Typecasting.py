# Please write a program which asks the user for a floating point number and then prints out the integer part and the decimal part separately. Use the Python int function. You can assume the number given by the user is always greater than zero.

# User gives a number
number = float(input("Please type in a number:"))

# Convert to integer
number_int = int(number)

# Find decimal by removing the integer part
number_decimal = number - number_int

print(f"Integer part: {number_int}")
print(f"Decimal part: {number_decimal}")
