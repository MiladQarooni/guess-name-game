import random

# library that we use in order to choose
# on random words from a list of words

name = input("What is your name? ")

# Here the user is asked to enter the name first

print("Good Luck ! ", name)

words = ['rainbow', 'computer', 'science', 'programming',
         'python', 'mathematics', 'player', 'condition',
         'reverse', 'water', 'board', 'geeks']

# Function will choose one random
# word from this list of words
word = random.choice(words)

# Get the len of word in words list
print(f"Your word has {len(word)} characters.")

# make a list with "-"

result_list = ["-" for _ in range(abs(len(word)))]

# a list to get the correct characters

list_word = []
x=len(word)
for i in range((len(word))):
    list_word.append(word[i])

# how many false char is entered
iword = 0

#them main loop
while True:
    char_word = input("Enter your char: ")

    if char_word in list_word:
        index_char = -1
        for i, char in enumerate(list_word):
            if char == char_word:
                index_char = i
                result_list[i] = char_word
        print(result_list)

        if "-" not in result_list:
            print("Congratulations! You win!")
            break

    else:
        iword += 1
        x -= 1
        print(f"You have {x} chances")

    if iword == len(word):
        print("You lose!")
        break
