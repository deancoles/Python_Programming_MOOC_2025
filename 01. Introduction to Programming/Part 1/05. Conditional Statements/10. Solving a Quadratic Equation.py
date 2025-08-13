"""
Please write a program for solving a quadratic equation of the form ax²+bx+c. The program asks for values a, b and c. It should then use the quadratic formula to solve the equation. 
The quadratic formula expressed with the Python sqrt function is:
x = (-b ± sqrt(b²-4ac))/(2a).
"""

# Import the sqrt function so we can take square roots
from math import sqrt

# Get values for a, b, and c from the user
a = int(input("Enter a value for a: "))
b = int(input("Enter a value for b: "))
c = int(input("Enter a value for c: "))

# Calculate the value under the square root in the formula
# (b**2 - 4ac) is sometimes called the "discriminant" in maths
value_under_sqrt = b**2 - (4 * a * c)

# Calculate both roots using the quadratic formula
# First root uses plus
root_1 = (-b + sqrt(value_under_sqrt)) / (2 * a)
# Second root uses minus
root_2 = (-b - sqrt(value_under_sqrt)) / (2 * a)

# Display the two roots
print(f"The roots are {root_1} and {root_2}")

