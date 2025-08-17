# Please write a program which keeps asking the user for words. If the user types in end or types in the same word twice in a row, the program should print out the story the words formed, and finish.

# Start with an empty sentence and no previous word
sentence = ""
previous = ""

while True:
    word = input("Please type in a word: ")

    # If the user types "end", stop and print the story
    if word == "end":
        print(sentence)
        break
    # If the word is the same as the last one entered, stop and print
    elif word == previous:
        print(sentence)
        break
    # Otherwise, add the word to the story and remember it as "previous"
    else:
        previous = word
        sentence += word + " "


# Alternate Solution

story = ""
previous = ""

while True:
    word = input("Please type in a word: ")

    if word == "end" or word == previous:
        break

    story += word + " "
    previous = word

print(story)
