"""
This program should print out a countdown. The code is as follows:

number = 5
print("Countdown!")
while True:
  print(number)
  number = number - 1
  if number > 0:
    break

print("Now!")

This should print out

Countdown!
5
4
3
2
1
Now!
"""

# Original Code
"""
number = 5
print("Countdown!")
while True:
  print(number)
  number = number - 1
  if number > 0:
    break

print("Now!")
"""

# Fixed Code

number = 5

# Print once before the loop
print("Countdown!")

while True:
    print(number)
    number = number - 1
    if number == 0:
        break

print("Now!")
