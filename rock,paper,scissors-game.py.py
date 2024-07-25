import random

option = ('rock','paper','scissors')
running = True

while running:

    player = None

    computer = random.choice(option)

    while player not in option:
        player = input("enter the choise game option(rock,paper,scissors)\n")

    print(f"player:{player}")   
    print(f"computer:{computer}")

    if player == computer:
        print("game tie")

    elif player == 'rock' and  computer == 'scissors':
        print("you win")
        
    elif player == 'paper' and  computer == 'rock':
        print("you win")

    elif player == 'scissor' and  computer == 'paper':
        print("you win")

    else:
        print("you loss")      

    if not input("play again? (y/n) : " ).lower() == "y": #y is yess, n is not
        running = False

print("thanks for playing")        
