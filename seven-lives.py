"""Copyright (c) 2022, Edward Jiang
All rights reserved.

This source code is licensed under the GNU General Public License found in the
LICENSE file in the root directory of this source tree."""

import random, sys, os, time # modules needed for this program

def write(word): # creates a writing letters one by one effect
  for ch in word:
    sys.stdout.write(ch)
    sys.stdout.flush()
    time.sleep(0.035)
  print()

def clear(): # clears the screen
  os.system('clear')
while True: # main loop of the program
    while True: # subloop that chooses difficulty
        write("Choose a difficulty:")
        print("A) Easy \nB) Normal \nC) Hard \nD) DEMON LEVEL")
        difficulty = input()
        if difficulty.lower() == 'a' or difficulty.lower() == 'easy':
            lives = 9
            words = ['kitty']
            secret_word = random.choice(words)
            break
        elif difficulty.lower() == 'b' or difficulty.lower() == 'normal':
            lives = 7
            words = ['assist','python','purple','yellow','orange','forever','camera','lights','chrome','google', 'challenge', 'keyboard', 'attack', 'change', 'queasy', 'console', 'mussel', 'muscle', 'mollusk']
            secret_word = random.choice(words)
            break
        elif difficulty.lower() == 'c' or difficulty.lower() == 'hard':
            words = ['interchange','interrogate','international','randomize','hurricane','seventeen','formation','gigantic','abundant','complicated', 'mitigate', 'vindicate', 'eradicate', 'repositioning', 'whereabouts', 'marketing', 'cetaceans', 'crustaceans']
            lives = 5
            secret_word = random.choice(words)
            break
        elif difficulty.lower() == 'd' or difficulty.lower() == 'demon level' or difficulty.lower() == 'demon':
            words = ['agglutinative', 'synesthesia', 'trustworthiness', 'xenotransplantation', 'interchangeable', 'acknowledgeable','personification', 'onomatopoeia', 'incomprehensibilities', 'photosynthesis', 'floccinaucinihilipilification', 'dichlorodifluoromethane', 'pneumonoultramicroscopicsilicovolcanoconiosis']
            lives = 3
            secret_word = random.choice(words)
            break
    clear()
    clue = []
    index = 0
    while index < len(secret_word): # fills the clue list with empty question marks
        clue.append("?")
        index += 1
    unknown_letters = len(secret_word) # amount of unguessed letters   
    heart = u'\u2764'
    guessed_word_correctly = False
    def get_indices(item, items): # returns the indices, or position(s) of item in items
        if item in items:
            counter = 0
            item_index = []
            for i in items:
                if i == item:
                    item_index.append(counter)
                counter = counter + 1
            return item_index
    def update_clue(guessed_letter, secret_word, clue, unknown_letters): # updates the question mark list, aka clue
        len_indices = 0
        for each in set(guessed_letter.lower()):
            each_index = get_indices(each, secret_word)
            for i in each_index:
                if clue[i] == "?":
                    del clue[i]
                    clue.insert(i, each)
                    len_indices += 1
                else:
                    continue
            
        unknown_letters -= len_indices
        return unknown_letters
    while lives > 0: # runs if you have more than 0 lives
        print(' '.join(clue))
        print('Lives left: ' + ' '.join(heart * lives))
        time.sleep(0.5)
        write("Guess a letter(s) or the whole word: ")
        guess = input()
        if guess.lower() == secret_word: # guess is the same as the secret word
            clear()
            guessed_word_correctly = True
            break
        if guess.lower() in secret_word: # guess is in the secret word
            clear()
            write("Your letter(s) is in the secret word!")
            time.sleep(1.25)
            unknown_letters = update_clue(guess, secret_word, clue, unknown_letters)
        else: # guess is not in the secret word
            clear()
            write("Your letter is not in the word, or you have guessed the word incorrectly. You have lost a life.")
            lives -= 1
            time.sleep(1.25)
        if unknown_letters == 0: # all letters guessed!
            clear()
            guessed_word_correctly = True
            break
    clear()
    if guessed_word_correctly == True: # if you guessed the word
        write("You won! The secret word was " + secret_word)
    elif guessed_word_correctly == False: # if you ran out of lives and did not get the word
        write("You lost! The secret word was " + secret_word)
    time.sleep(1.25)
    play_again = input("Play again [yes/no]? ") # asks user to play again
    if play_again.lower() == 'no' or 'n': # quits program
        break
    else: # returns to start
        clear()
        continue
