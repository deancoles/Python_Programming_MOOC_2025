# Please write a program which asks the user for a word and then prints out the number of characters, if there was more than one typed in.

# User inputs word, length is determined
word = input("Please type in a word:")
word_length = len(word)

# Execute this if length is greater than one
if word_length > 1:
    print(f"There are {word_length} letters in the word {word}")

print("Thank you!")
