# Please write a program which asks the user for a year, and prints out the next leap year.

year = int(input("Year: "))
next_year = year + 1
leap_year = False

# Loop until a leap year is found
while True:
    if next_year % 400 == 0:
        leap_year = True
    elif next_year % 100 == 0:
        leap_year = False
    elif next_year % 4 == 0:
        leap_year = True
    
    if leap_year == True:
        print(f"The next leap year after {year} is {next_year}")
        break
    else:
        next_year += 1


# Alternate Solution

start_year = int(input("Year: "))
year = start_year + 1

while True:
    if year % 100 == 0:
        if year % 400 == 0:
            break
    elif year % 4 == 0:
        break

    year += 1

print(f"The next leap year after {start_year} is {year}")
