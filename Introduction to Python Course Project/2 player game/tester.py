import random 
import time

def play_game():
    player1 = input("Player 1, choose rock, paper or scissors -").lower()
    print("\033[H\033[J")
    time.sleep(5)
    player2 = input("Player 2 choose rock, paper or scissors -").lower()
    print("\033[H\033[J")
    time.sleep(5)
        
    if player1 =="rock" and player2 == "paper":
        print("Well done Player 2, you have won!")

    elif player1 =="scissors" and player2 == "rock":
        print("Well done Player 2, you have won!")

    elif player1 =="paper" and player2 == "scissors":
        print("Well done Player 2, you have won!")

    elif player1 == player2:
        print("So close, it's a tie!")

    else:
        print ("Well done Player 1, you have won!")

# Starting code
print("Welcome to rock, paper, scissors")
play_game()









#https://www.quora.com/How-do-I-hide-the-last-line-of-code-that-I-used-using-Python-For-example-if-I-was-writing-a-trivia-game-and-I-wanted-the-intro-to-disappear-after-3-seconds-do-I-have-to-define-the-function-myself#:~:text=To%20hide%20the%20last%20line%20of%20code%20that%20you%20used,before%20the%20line%20is%20displayed.
#https://thecleverprogrammer.com/2022/05/12/rock-paper-scissors-game-using-python/  
#Programming Python by Mark Lutz