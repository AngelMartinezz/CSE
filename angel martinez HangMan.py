import random
import string

"""
A general guide for Hangman
1. Make a word bank - 10 times
2. Pick a random item for the list
3. Hide the word (use*)
4. Reveal letters already guessed
5. Create the win condition

 """
guesses_left = 10

word_bank = ["chips", "games","movies","phone","clock","desk","people","jucie","shoes","books"]
random_word = word_bank[random.randint(0, len (word_bank)-1)]
# print(random_word)
letters_guessed = []

current_guess = ''

while guesses_left:
    output = []
    for letter in random_word:
        if letter in letters_guessed:
            output.append(letter)
        else:
            output.append("*")
    print(output)
    guess = input("Guess a letter: ")
