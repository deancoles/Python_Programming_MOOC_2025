# Please write a program which asks for tomorrow's weather forecast and then suggests weather-appropriate clothing. The suggestion should change if the temperature is over 20, 10 or 5 degrees, and also if there is rain on the radar.

# user input for temperature and rain
temp = int(input("What is the temperature? "))
rain = input("Will it rain (yes/no): ").lower()

print("What is the weather forecast for tomorrow?")
print(f"Temperature: {temp}")
print(f"Will it rain (yes/no): {rain}")

# Will always print, regardless of temperature and rain
print("Wear jeans and a T-shirt")

# Statements to print depending on temperature and rain, can print multiple of these
if temp <= 20:
    print("I recommend a jumper as well")
if temp <= 10:
    print("Take a jacket with you")
if temp <= 5:
    print("Make it a warm coat, actually")
    print("I think gloves are in order")
if rain == "yes":
    print("Don't forget your umbrella!")
