# Seven-Lives
A simple linguistics word-guessing game
# Updates (most recent at top)
## Update v0.2.1
- Bug fixes
- Better system for fault tolerance
- This is the bigger fix I was talking about—now its complete, so yay!
- To break the bigger fix down into detail, I have now updated the code to work with more varied guesses from the user, or in other words, the user can input a more wider variety of guesses using combinations of letters, and the code will handle that much better. ***In earlier versions, the user had a limited field of input, and the updated update_clue() function can now work with much more. Let's take a look at how it works. So first, the update_clue() function looks at the guessed input (Note: the update_clue function only runs if the input is in the word). It also creates a new variable every time it is called, len_indices. This variable keeps count of the correct letters and at the end will be subtracted from unknown_letters. Once unknown_letters reaches 0, the game ends. Ok, back to what we were talking about. The function will first start a for loop that loops through each character in the guess (it has also become even smarter to use the built-in set() function to remove repeats in the guess). Then, it will use get_indices() to get the index (or indices) of the letter in the secret word. ***
## Update v0.1.1
- Bug fixes
- Bigger fix currently in progress, so it will not work for now
## Update v0.1.0
- Yay! Seven-Lives is now published
- More updates to come in the future, so stay tuned!
