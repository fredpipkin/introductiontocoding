# introductiontocoding
Assignment for introduction to coding

This Python code implements a simple Rock, Paper, Scissors game for two players using keyboard inputs. Here's a summary of the code:

The code uses the keyboard module, so it starts by installing it using pip install keyboard in the terminal.

There are three main functions defined:

get_player_choices(): Continuously checks for keyboard inputs from players until both have made a choice (Rock, Paper, or Scissors).
get_game_result(p1, p2): Determines the game result based on the choices made by Player 1 (p1) and Player 2 (p2).
play_game(): Initiates the game by printing a countdown, getting player choices, determining the result, and displaying it. Then, the game pauses for 5 seconds before potentially starting a new round.
The main loop (while True) presents a welcome message and instructions for players, allowing them to input choices using specific keys. The game then prompts the user to type 'q' to quit or anything else to start a new round.

If the user types 'q', the program exits with a goodbye message. Otherwise, it proceeds to play a round by calling the play_game() function.

In summary, this code provides a simple Rock, Paper, Scissors game for two players with keyboard inputs and a user-friendly interface.The game also ensures that the players do not know each others choices until the winner is revelaed. 
The game loop allows users to play multiple rounds or quit at any time.

Reference points while coding the game are as follows - 
  
  https://stackoverflow.com/questions/24072790/how-to-detect-key-presses
  
  https://www.quora.com/How-do-I-hide-the-last-line-of-code-that-I-used-using-Python-For-example-if-I-was-writing-a-trivia-game-and-I-wanted-the-intro-to-disappear-after-3-seconds-do-I-have-to-define-the-function-myself#:~:text=To%20hide%20the%20last%20line%20of%20code%20that%20you%20used,before%20the%20line%20is%20displayed.

  https://thecleverprogrammer.com/2022/05/12/rock-paper-scissors-game-using-python/  
Programming Python by Mark Lutz

