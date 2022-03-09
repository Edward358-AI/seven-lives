import random, sys, os, time

def write(word):
  for ch in word:
    sys.stdout.write(ch)
    sys.stdout.flush()
    time.sleep(0.035)
  print()

def clear():
  os.system('clear')
while True:
    while True:
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
    while index < len(secret_word):
        clue.append("?")
        index += 1
    unknown_letters = len(secret_word)    
    heart = u'\u2764'
    guessed_word_correctly = False
    def get_indices(item, items):
        if item in items:
            counter = 0
            item_index = []
            for i in items:
                if i == item:
                    item_index.append(counter)
                counter = counter + 1
            return item_index
    def update_clue(guessed_letter, secret_word, clue, unknown_letters):
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
    while lives > 0:
        print(' '.join(clue))
        print('Lives left: ' + ' '.join(heart * lives))
        time.sleep(0.5)
        write("Guess a letter(s) or the whole word: ")
        guess = input()
        if guess.lower() == secret_word:
            clear()
            guessed_word_correctly = True
            break
        if guess.lower() in secret_word:
            clear()
            write("Your letter(s) is in the secret word!")
            time.sleep(1.25)
            unknown_letters = update_clue(guess, secret_word, clue, unknown_letters)
        else:
            clear()
            write("Your letter is not in the word, or you have guessed the word incorrectly. You have lost a life.")
            lives -= 1
            time.sleep(1.25)
        if unknown_letters == 0:
            clear()
            guessed_word_correctly = True
            break
    clear()
    if guessed_word_correctly == True:
        write("You won! The secret word was " + secret_word)
    elif guessed_word_correctly == False:
        write("You lost! The secret word was " + secret_word)
    time.sleep(1.25)
    play_again = input("Play again [yes/no]? ")
    if play_again.lower() == 'no' or 'n':
        break
    else:
        clear()
        continue
