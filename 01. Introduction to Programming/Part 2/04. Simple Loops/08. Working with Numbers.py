"""
- Please write a program which asks the user for integer numbers. The program should keep asking for numbers until the user types in zero.
- After reading in the numbers the program should print out how many numbers were typed in.
- The program should also print out the sum of all the numbers typed in. 
- The program should also print out the mean of the numbers.
- The program should also print out statistics on how many of the numbers were positive and how many were negative.
"""

count= 0		# How many numbers have been entered
sum_num = 0		# The total of these numbers
pos_num = 0		# Counts positive numbers
neg_num = 0		# Counts negative numbers

print("Please type in integer numbers. Type in 0 to finish.")

while True:
    num = int(input("Number:"))
    
    count+=1			# Add to count
    sum_num += num	    # Add to sum

    if num < 0:
        neg_num += 1	# Add to negative numbers
    
    if num > 0:
        pos_num += 1	# Add to positive number

    if num == 0:
        count-=1		# Remove from count
        print(f"Numbers typed in {count}")
        print(f"The sum of the numbers is {sum_num}")
        print(f"The mean of the numbers is {sum_num / count}")
        print(f"Positive numbers {pos_num}")
        print(f"Negative numbers {neg_num}")
        break
        

# Alternate Solution

print("Please type in integer numbers. Type in 0 to finish.")

numbers = 0
sum = 0
positives = 0

while True:
    number = int(input("Number: "))

    if number == 0:
        break

    numbers += 1
    sum += number

    if number>0:
        positives += 1

print("Numbers typed in", numbers)
print("The sum of the numbers is", sum)
print("The mean of the numbers is", sum/numbers)
print("Positive numbers", positives)
print("Negative numbers", numbers-positives)
