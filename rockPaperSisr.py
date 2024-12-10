import random as r

print("Welcome to Rock Paper Scissors Game!")
# Rules
print("Here are the rules: \n1. Rock beats Scissors \n2. Scissors beats Paper \n3. Paper beats Rock")

players_input = int(input("Please select one \n options \n 1.Rock \n 2.Paper \n 3.Scissors \n Please select your option here(1/2/3): "))


rock ="""
                        _______
                    ---'   ____)
                        (_____)
                        (_____)
                        (____)
                    ---.__(___)
                    """
paper ="""
                         _______
                    ---'    ____)____
                               ______)
                              _______)
                             _______)
                    ---.__________)
                    """

scissors = """
                        _______
                    ---'   ____)____
                              ______)
                           __________)
                          (____)
                    ---.__(___)
                    """

figres =[rock,paper,scissors]



print("Player's input")
if players_input == 1:
    print(figres[players_input-1])
    print("Rock")
elif players_input == 2:
    print(figres[players_input-1])
    print("Paper")
elif players_input == 3:
    print(figres[players_input-1])
    print("Scissors")
else:
    print("Invalid Selection \n Game Over !!!!")
    exit()

print("Computer's turn")
computer_input = r.randint(1, 3)
print("Computer's input")

if computer_input == 1:
    print(figres[computer_input-1])
    print("Rock")
elif computer_input == 2:
    print(figres[computer_input-1])
    print("Paper")
elif computer_input == 3:
    print(figres[computer_input-1])
    print("Scissors")

# Comparing the inputs
if players_input == computer_input:
    print("It's a tie!")
elif (players_input == 2 and computer_input == 1) or (players_input == 1 and computer_input == 3) or (players_input == 3 and computer_input == 2):
    print("Player wins!")
else:
    print("Computer wins!")
