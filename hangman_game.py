import random


max_choice = 10
words_list = ['Awkward', 'Bagpipes', 'Banjo', 'Bungler', 'Croquet', 'Crypt', 'Dwarves', 'Fervid', 'Fishhook', 'Fjord',
              'Gazebo', 'Gypsy', 'Haiku', 'Haphazard', 'Hyphen', 'Ivory', 'Jazzy', 'Jiffy', 'Jinx', 'Jukebox', 'Kayak',
              'Kiosk', 'Klutz', 'Memento', 'Mystify', 'Numbskull', 'Ostracize', 'Oxygen', 'Pajama', 'Phlegm', 'Pixel',
              'Polka', 'Quad', 'Quip', 'Rhythmic', 'Rogue', 'Sphinx', 'Squawk', 'Swivel', 'Toady', 'Twelfth', 'Unzip',
              'Waxy', 'Wildebeest', 'Yacht', 'Zealous', 'Zigzag', 'Zippy', 'Zombie']


def print_word(w_list):
    return "".join(w_list).replace('_', '__ ')


def add_char_guess_word(char_arg, g_word, word_arg):
    for index, let in enumerate(word_arg):
        if char_arg == let:
            g_word.insert(index, char_arg)
            del g_word[index + 1]
    return g_word


print("Hi Welcome to Hangman Game")
print("You will be given 10  to guess the word.\nEach time you can guess a letter from the word.\n")
print("Let's start the game")

word = (random.choice(words_list)).lower()
print(word)
word_length = len(word)
guess_word = list("_" * word_length)
print(f"Here is your word of len {word_length}!!")
for i in range(max_choice):
    print(print_word(guess_word))
    char = (input(f"Chance {i+1}:Guess a letter ? ")).lower()
    if char not in word:
        print("No letters of your choice in the word to be guessed.\n")
        if i != max_choice:
            print("Lets us continue...")
            continue
    else:
        print("Great!!Good Guess")
        guess_word = add_char_guess_word(char, guess_word, word)

        if word == print_word(guess_word):
            print("You guessed the word ..Perfect..\nYou won!!! ")
            break
        print("Here is your word ..\n")
        print(print_word(guess_word))
        opt = input("Do you need to guess the word.(y/n)")
        if opt.lower() == 'y':
            complete_word = input("Guess the word ?")
            if complete_word == word:
                print("Perfect...You won the game ..")
                break
            else:
                print("Try next time..\nLet's continue the game..")
        elif opt.lower() == 'n':
            print("Let us continue the game.. ")
        else:
            print("Hope you don't want to guess..\nLet's continue ...")

print("Come again soon....")
