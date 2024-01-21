#run pip install keyboard in terminal
import keyboard
import time

def get_player_choices():
    choices = {'p1': None, 'p2': None}

    while None in choices.values():
        if keyboard.is_pressed('z'):
            choices['p1'] = 'Rock'
        elif keyboard.is_pressed('x'):
            choices['p1'] = 'Paper'
        elif keyboard.is_pressed('c'):
            choices['p1'] = 'Scissors'

        if keyboard.is_pressed('1'):
            choices['p2'] = 'Rock'
        elif keyboard.is_pressed('2'):
            choices['p2'] = 'Paper'
        elif keyboard.is_pressed('3'):
            choices['p2'] = 'Scissors'

    return choices
#lines 5 to 23 defines the players inputs and matches it using if/elif to the corrospoding rock, paper or scissors.

def get_game_result(p1, p2):
    if p1 == p2:
        result = 'Draw!'
    elif p1 == 'Scissors':
        if p2 == 'Rock':
            result = 'Player 2 wins!'
        elif p2 == 'Paper':
            result = 'Player 1 wins!'
    elif p1 == 'Paper':
        if p2 == 'Scissors':
            result = 'Player 2 wins!'
        elif p2 == 'Rock':
            result = 'Player 1 wins!'
    elif p1 == 'Rock':
        if p2 == 'Scissors':
            result = 'Player 1 wins!'
        elif p2 == 'Paper':
            result = 'Player 2 wins!'

    return '%s v %s, %s' % (p1, p2, result)
#26 to 45 outlines the possible results from the game with each user input using the if/elis funct again.
def play_game():
    count_pause = 0.5

    print('Ready!') 
    time.sleep(count_pause)
    print('3!') 
    time.sleep(count_pause)
    print('2!') 
    time.sleep(count_pause)
    print('1!') 
    time.sleep(count_pause)
    print('Go!') 
    choices = get_player_choices()
    final_message = get_game_result(choices['p1'], choices['p2'])
    print(final_message)
    time.sleep(5)
#TO make the game a bit more interesting, I used time.sleep to output a countdown for the game to begin! Line 59 fetches the choices and outputs final message.
#After, the game will pause for 5 seconds to break up the rounds before asking the player if they want to play again or quit (see lines 78 and 80).

# Starting point
while True:
    print('Welcome to Rock, Paper, Scissors!')
    print('Player One keys')
    print('z - Rock')
    print('x - Paper')
    print('c - Scissors')
    print('Player Two keys')
    print('1 - Rock')
    print('2 - Paper')
    print('3 - Scissors')
    print('')
    response = input('Type q to quit or anything else to start a new game').lower()
    
    if response == 'q':
        print('Goodbye!')
        break
    else:
        play_game()

# https://stackoverflow.com/questions/24072790/how-to-detect-key-presses
#https://www.quora.com/How-do-I-hide-the-last-line-of-code-that-I-used-using-Python-For-example-if-I-was-writing-a-trivia-game-and-I-wanted-the-intro-to-disappear-after-3-seconds-do-I-have-to-define-the-function-myself#:~:text=To%20hide%20the%20last%20line%20of%20code%20that%20you%20used,before%20the%20line%20is%20displayed.
#https://thecleverprogrammer.com/2022/05/12/rock-paper-scissors-game-using-python/  
#Programming Python by Mark Lutz