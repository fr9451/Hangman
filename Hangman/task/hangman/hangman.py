# Write your code here
import random
import string


def game():
    menu = input('Type "play" to play the game, "exit" to quit: ')
    if menu == 'play':
        hangman()
    elif menu == 'exit':
        return False


def game_menu():
    print('H A N G M A N')
    menu = input('Type "play" to play the game, "exit" to quit: ')
    if menu == 'play':
        hangman()
    elif menu == 'exit':
        return False


word_list = ['python', 'java', 'kotlin', 'javascript']

chosen = random.choice(word_list)


def hangman():
    tries = 8
    hide = '-' * len(chosen)
    attempted_letters = []
    while tries != 0:
        print()
        print(hide)
        letters = input('Input a letter:')
        attempted_letters.append(letters)
        for index, letter in enumerate(chosen):
            if letter == letters:
                guessed = list(hide)
                guessed[index] = letters
                hide = ''.join(guessed)
        if attempted_letters.count(letters) > 1:
            print('You already typed this letter')
        elif letters not in hide and letters in string.ascii_lowercase:
            print('No such letter in the word')
            tries -= 1
        if letters not in string.ascii_lowercase and len(letters) == 1:
            print('It is not an ASCII lowercase letter.')
        if len(letters) > 1:
            print('You should input a single letter')
        if hide == chosen:
            print()
            print(chosen)
            print('You guessed the word!')
            print('You survived!')
            print()
            game()
            break
        if tries == 0:
            print('You are hanged!')
            print()
            game()
            break


game_menu()
