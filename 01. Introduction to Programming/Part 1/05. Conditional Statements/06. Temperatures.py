# Please write a program which asks the user for a temperature in degrees Fahrenheit, and then prints out the same in degrees Celsius. If the converted temperature falls below zero degrees Celsius, the program should also print out "Brr! It's cold in here!".

# user inputs temperature in fahrenheit
temp = int(input("Please type in a temperature(F):"))

# Fahrenheit converted to Celsius
celsius = (temp -32) * 5 / 9

# Show the user the result
print(f"{temp} degrees Fahrenheit equals {celsius} degrees Celsius")

# Print a message if temperature drops below zero.
if celsius <0:
    print("Brr! It's cold in here!")
