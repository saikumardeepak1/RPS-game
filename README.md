# Rock-Paper-Scissors-Game

This code is a simple implementation of the popular Rock-Paper-Scissors game.
At the start, the program prints a welcome message for the user and initializes the
scores of the user and the computer to zero.

Inside the while loop, the program generates a random move for the computer using the 
randint() function of the random module. The program then prompts the user to enter their move, 
and the input is converted to lowercase using the lower() function.

If the user enters "q", the program quits, and the loop is terminated. If the user enters 
an invalid input, the loop continues. If the user and the computer make the same move, the 
program informs the user that the result is a tie. If the user wins, the program increments 
the user's score. If the computer wins, the program increments the computer's score.

The program continues until the user quits the game. Once the game is over, the program prints 
the final scores of the user and the computer and ends.

The functionality of the code is to allow the user to play a game of Rock-Paper-Scissors against 
the computer and keep track of their scores.

The level of the project is beginner to intermediate, as it involves basic concepts of 
programming like loops, conditionals, and functions. It is also an excellent example of 
how to implement a simple game using Python.
