# Step 1
#TO DO List
#1.Randomly choose a word from word list and assign it to a variable choosen_word. then print it 
#2.Ask the user to guess a letter and assign it to a variable guess.make it lower case
#3.check if the letter user guessed is one of the word in the choosen_word print "Right" if it is else "Wrong.

#Step 2 
'''    1: cre 3edaete a empty string called placeholder
       2: for each letter in the choosen_word add a placeholder
       3:so if the choosen_word is apple the placeholder should be _ _ _ _ _
       4: if the user is guessed p then and the choosen word was apple then
       the output should be _ p p _ _
'''



import random as r
# import the stages.py module
import includes.stages as s
import includes.hangmanWords as w
word_list = w.words
blank='_'
choosen_word=r.choice(word_list)
print(s.logo[0])
print(choosen_word)  
placeholder=len(choosen_word)*blank
print(placeholder)
guess_completed=False
correct_guess=[]
stage=s.stages
lives=6
while not guess_completed:
    display=''
    guess=str(input("Guess a letter :")).lower()
    if not guess in correct_guess:
        if guess in choosen_word:
            for letter in choosen_word:
                    if letter == guess:
                        display+=letter
                        correct_guess.append(letter)
                    elif letter in correct_guess:
                        display+=letter
                    else:
                        display+=blank
            print(stage[lives])
            if blank not in display:
                guess_completed=True

                print(f"You Won the word is {display}")
        else:
            lives-=1
            print(f"Wrong guess. You have {lives}/6 lives left")
            print(stage[lives])
            if lives == 0:
                print("Game Over")
                guess_completed=True
                print(f"The correct word was {choosen_word}")
    else:
        print(f"You have already guessed {guess}")
        print(display)




