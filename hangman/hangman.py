import random
import string
import sys

from words import words

def get_valid_word(words):
    word = random.choice(words)
    while '-' in word or ' ' in word:
        word = random.choice(words)

    return word.upper()

def play_again():
    pa = ''
    while pa.upper() != 'Y' or pa.upper() != 'N':
        pa = input('Would you like to play again? (Y) (N)\n')
        if pa.upper() == 'Y':
            hangman()
        elif pa.upper() == 'N':
            print('It has been fun! See you again soon.')
            sys.exit()
        else:
            print('Invalid input, please enter either Y or N...')

def hangman():
    word = get_valid_word(words)
    guessed_letters = set()
    unguessed_letters = set(word)
    alphabet = set(string.ascii_uppercase)

    starting_lives = 9

    lives = starting_lives

    def picture():
        if starting_lives - lives == 0:
            print("""
   ___
  |   |
      |
      |
      |
    -----""")
        elif starting_lives - lives == 1:
            print("""
   ___
  |   |
  O   |
      |
      |
    -----""")
        elif starting_lives - lives == 2:
            print("""
   ___
  |   |
  O   |
  |   |
      |
    -----""")
        elif starting_lives - lives == 3:
            print("""
   ___
  |   |
  O   |
 /|   |
      |
    -----""")
        elif starting_lives - lives == 4:
            print("""
   ___
  |   |
  O   |
 /|\  |
      |
    -----""")
        elif starting_lives - lives == 5:
            print("""
   ___
  |   |
  O   |
 /|\  |
 /    |
    -----""")
        elif starting_lives - lives == 6:
            print("""
   ___
  |   |
  O   |
 /|\  |
 / \  |
    -----""")
        elif starting_lives - lives == 7:
            print("""
   ___
  |   |
  O   |
 /|\  |
_/ \  |
    -----""")
        elif starting_lives - lives == 8:
            print("""
   ___
  |   |
  O   |
 /|\  |
_/ \_ |
    -----""")
        else:
            print("""
   ___
  |   |
  0   |
 /|\  |
_/ \_ |
    -----""")

    while len(unguessed_letters) > 0 and lives > 0:
        print('\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n')
        print(f'Lives left: {lives}\nYou have used these letters: ', ''.join(guessed_letters))
        word_list = [letter if letter in guessed_letters else '_' for letter in word]
        picture()
        print('Current Word: ', ' '.join(word_list))
        user_guess = input('Enter a Letter to Guess: ').upper()
        if user_guess in alphabet - guessed_letters:
            guessed_letters.add(user_guess)
            if user_guess in unguessed_letters:
                unguessed_letters.remove(user_guess)
            else:
                lives = lives -1
                print('Letter is not in the word')
        elif user_guess in guessed_letters:
            print('You have already guessed that character, try again.')
        else:
            print('Invalid character')
    if lives == 0:
        print('\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n')
        picture()
        print(f'You have killed Mr. H. Man, the word was: {word[0]}{word.lower()[1:]}')
        play_again()
    else:
        print('\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n')
        picture()
        print(f'Congrats you got the word, {word[0]}{word.lower()[1:]}, with {lives} lives left! ')
        play_again()

hangman()
