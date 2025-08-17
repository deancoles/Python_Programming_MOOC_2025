# Please write a program which asks for two integer numbers. The program should then print out whichever is greater. If the numbers are equal, the program should print a different message.

num_1 = int(input("Please type in the first number:"))
num_2 = int(input("Please type in another number:"))

# Run code block depending on the numbers given
if num_1 > num_2:
    print(f"The greater number was: {num_1}")
elif num_2 > num_1:
    print(f"The greater number was: {num_2}")
elif num_1 == num_2:
    print(f"The numbers are equal")
