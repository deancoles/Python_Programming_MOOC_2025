"""
Please write a program which asks the user for a number of days. The program then prints out the number of seconds in the amount of days given.

The program should function as follows:
Sample output

How many days? 1
Seconds in that many days: 86400
"""

# User inputs a number of days
days = int(input("How many days?"))

# Calculation for a single day's seconds, being hours times (minutes times seconds).
day_seconds = 24 * (60 * 60) 

print(f"Seconds in that many days: {days * (day_seconds)}")
