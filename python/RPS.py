import random

comp=("Rock","Paper","Scissor")
comp=random.choice(comp)
def game():
    player=input("Rock,Paper or Scissors?: ")
    if player == 'rock':
        print("I choose:",comp)
        if comp == "Rock":
            print("its a tie")
        elif comp == "Paper":
            print("you lose")
        else:
            print("you won")
    elif player == 'paper':
        print("I choose:",comp)
        if comp == "Paper":
            print("its a tie")
        elif comp == "Scissor":
            print("you lose")
        else:
            print("you won")
    elif player == 'scissor':
        print("I choose:",comp)
        if comp == "Scissor":
            print("its a tie")
        elif comp == "Rock":
            print("you lose")
        else:
            print("you won")


game()