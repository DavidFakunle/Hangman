import random
#use the 'word_list' from hangman_words.py

from hangman_words import *
chosen_word = random.choice(word_list)
word_length = len(chosen_word)

end_of_game = False
lives = 6

#- Import the logo from hangman_art.py and display it at the start of the game.
from hangman_art import *
print(logo)
#Testing code

#Create blanks
display = []
for _ in range(word_length):
    display += "_"
print(display)
while not end_of_game:
    guess = input("Guess a letter: ").lower()
    if  type(guess) != str:
      print("Error please type in a letter")

    #If the user has entered a letter they've already guessed, print the letter and let them know.
    if guess in display and chosen_word:
      print(f'You have already guess the letter {guess}')
    #Check guessed letter
    for position in range(word_length):
        letter = chosen_word[position]
        #print(f"Current position: {position}\n Current letter: {letter}\n Guessed letter: {guess}")
        if letter == guess:
            display[position] = letter

    #Check if user is wrong.
    if guess not in chosen_word:
        #If the letter is not in the chosen_word, print out the letter and let them know it's not in the word.
        print(f'You guessed {guess}, thats not in the word. You lose a life.')
        lives -= 1
        print(f"You have {lives} lives left")
        if lives == 0:
            end_of_game = True
            print("You lose.")
            print(f'The word was: {chosen_word}')
   

    #Join all the elements in the list and turn it into a String.
    print(f"{' '.join(display)}")

    #Check if user has got all letters.
    if "_" not in display:
        end_of_game = True
        print("You win.")

   # Import the stages from hangman_art.py and make this error go away.
    from hangman_art import *
    print(stages[lives])
    