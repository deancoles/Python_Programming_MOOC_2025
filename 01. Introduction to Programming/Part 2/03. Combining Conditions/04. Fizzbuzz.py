# Please write a program which asks the user for an integer number. If the number is divisible by three, the program should print out Fizz. If the number is divisible by five, the program should print out Buzz. If the number is divisible by both three and five, the program should print out FizzBuzz.

# User gives number
number = int(input("Please enter a number:"))

# Print out depends on number
if number % 3 == 0 and number % 5 == 0:     # This condition must be evaluated first, because if true, the other two conditions are also true
    print("FizzBuzz")
elif number % 3 == 0:
    print("Fizz")
elif number % 5 == 0:
    print("Buzz")


