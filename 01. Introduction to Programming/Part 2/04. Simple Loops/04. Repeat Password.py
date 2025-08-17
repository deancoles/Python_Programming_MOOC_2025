# Please write a program which asks the user for a password. The program should then ask the user to type in the password again. If the user types in something else than the first password, the program should keep on asking until the user types the first password again correctly.

password = input("Password: ")

# Keep asking until the user repeats the password correctly
while True:
    repeat = input("Repeat password: ")

    # If the repeated password doesn't match the original, show an error
    if repeat != password:
        print("They do not match!")
    else:
        break

print("User account created!")
