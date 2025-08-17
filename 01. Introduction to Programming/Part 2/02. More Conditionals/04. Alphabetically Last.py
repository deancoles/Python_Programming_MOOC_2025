# Please write a program which asks the user for two words. The program should then print out whichever of the two comes alphabetically last.

word_1 = input("Please type in the 1st word:").lower()
word_2 = input("Please type in the 2nd word:").lower()

# First word is alphabetically later
if word_1 > word_2:
    print(f"{word_1} comes alphabetically last.")
# Second word is alphabetically later
elif word_2 > word_1:
    print(f"{word_2} comes alphabetically last.")
# Both words are exactly the same
elif word_1 == word_2:
    print("You gave the same word twice.")
