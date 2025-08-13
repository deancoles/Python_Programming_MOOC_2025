# Please write a program which asks for the user's name. If the name is anything but "Jerry", the program then asks for the number of portions and prints out the total cost. The price of a single portion is 5.90.

# User input
name = input(f"Please tell me your name:")

# If user's name is Jerry, refuse to serve, otherwise continue to serve customer
if name == "Jerry":
    print("Next please!")
else:
    portions = int(input("How many portions of soup?"))     
    print(f"The total cost is {portions * 5.90}")           # Portions times cost
    print("Next please!")
