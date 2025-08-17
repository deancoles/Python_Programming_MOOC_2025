# Please write a program which keeps asking the user for a PIN code until they type in the correct one, which is 4321. The program should then print out the number of times the user tried different codes.

attempts = 0

# Loop until the correct PIN is entered
while True:
    pin = input("PIN: ")
    attempts += 1

    # If PIN is correct
    if pin == "4321":
        if attempts == 1:
            print("Correct! it only took you one single attempt!")
            break
        # PIN correct but took more than one attempt
        else:
            print(f"Correct! It took you {attempts} attempts")
            break
    else:
        print("Wrong")

# Alternate Solution

# Start attempt counter at 1, because the user will immediately be asked once
attempts = 1

# Loop until the correct PIN is entered
while True:
    pin = input("PIN: ")
   
# If PIN is correct, exit the loop immediately
    if pin == "4321":
        break

    # If wrong, inform the user and increase attempt count
    print("Wrong")
    attempts += 1

# At this point the loop has ended, so the PIN must be correct
if attempts == 1:
    print("Correct! It only took you one single attempt!")
else:
    print(f"Correct! It took you {attempts} attempts")

