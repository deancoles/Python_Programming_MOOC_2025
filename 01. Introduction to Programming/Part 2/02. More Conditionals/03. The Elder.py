# Please write a program which asks for the names and ages of two persons. The program should then print out the name of the elder.

# Enter name and age of two people
p1_name = input("Please enter a name")
p1_age = int(input("Now enter their age"))
p2_name = input("Please enter another name")
p2_age = int(input("Now enter their age"))

# Three possible scenarios
if p1_age > p2_age:
    print(f"The elder is {p1_name}")
if p2_age > p1_age:
    print(f"The elder is {p2_name}")
if p1_age == p2_age:
    print(f"{p1_name} and {p2_name} are the same age")
