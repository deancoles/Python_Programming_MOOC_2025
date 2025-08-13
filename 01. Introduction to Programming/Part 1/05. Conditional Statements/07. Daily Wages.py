# Please write a program which asks for the hourly wage, hours worked, and the day of the week. The program should then print out the daily wages, which equal hourly wage multiplied by hours worked, except on Sundays when the hourly wage is doubled.

# User inputs
hour_wage = float(input("Enter hourly wage"))
hour_work = int(input("Enter hours worked"))
day = input("Enter the day of the week")

# If day is Sunday, give double wages, otherwise give regular
if day == "Sunday":
    print(f"Daily wages: {(hour_wage * 2) * hour_work} euros")   # Wages (x2) times hours
else:
    print(f"Daily wages: {hour_wage * hour_work} euros")         # Wages times hours
