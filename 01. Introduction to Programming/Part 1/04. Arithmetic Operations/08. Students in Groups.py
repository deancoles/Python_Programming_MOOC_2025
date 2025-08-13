# Please write a program which asks for the number of students on a course and the desired group size. The program will then print out the number of groups formed from the students on the course. If the division is not even, one of the groups may have fewer members than specified.

# User inputs students and desired group size
students = int(input("How many students on the course?"))
size = int(input("Desired group size?"))

# Work out how many completely full groups we can make (ignoring any leftover students)
groups = students // size

# If there are leftover students (remainder not zero), add one more group
if students % size != 0:
    groups = groups +1
else:
    groups = groups

print(f"Number of groups formed: {groups}")
