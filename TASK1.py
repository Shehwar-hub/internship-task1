import random

while True:
    print("WELCOME TO ROCK, PAPER, SCISSOR GAME!!!")
    move = input("What's your move (rock,paper,scissor)? Type'end' to quit: ".lower())
    if move == "end":
        print("Quiting the game.\nThank You!")
        break
    elif move in ["rock","paper","scissors"]:
        comp_move = random.choice(["rock","paper","scissors"])
        print("Computer move: ",comp_move.capitalize())
        print("Your move:",move.capitalize())
        if move == comp_move:
            print("It's a TIE")
        elif ((move == "rock" and comp_move == "scissors") or (move == "scissors" and comp_move == "paper") or (move == "paper" and comp_move == "rock")):
            print("Congratulations!! You Won")
        else:
            print("Computer Won")

    else:
        print("Invalid move...")
