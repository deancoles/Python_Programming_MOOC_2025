# This program should print out the message "hi" and then ask "Shall we continue?" until the user inputs "no". Then the program should print out "okay then" and finish.

# Keep looping until the user explicitly types "no"
while True:
    print("hi")
    question = input("Shall we continue?").lower()

    if question == "no":
        break
print("okay then")
