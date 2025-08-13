"""
Here is a program which should ask for three utterances and print them out, like so:
Sample output

The 1st part: hickory
The 2nd part: dickory
The 3rd part: dock
hickory-dickory-dock!

However, there is something wrong with the code below. Please fix it.
"""

# Original Code
"""
part = input("The 1st part: ")
part = input("The 1st part: ")
part = input("The 1st part: ")
print(part + part + part)
"""

# Fixed Code
part_1 = input("The 1st part: ")
part_2 = input("The 2nd part: ")
part_3 = input("The 3rd part: ")
print(part_1 + "-" + part_2 + "-" + part_3 + "!")


