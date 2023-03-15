import random

print("Welcome to Rock Paper Scissors game.\nYou are now competing with a Computer")

options = ["rock", "paper", "scissors"]

you = 0

Computer = 0

while True:
    Computer_input = random.randint(0,2)
    Computer_input = options[Computer_input]
    user_input = input("Choose Rock/ Paper/ Scissors/ Q to Quit:").lower()
    if user_input == "q":
        print("Quitting......\nyou left the game")
        break
    elif user_input not in options:
        continue
    elif user_input == Computer_input:
        print(f"{Computer_input} vs {user_input}\nYou both selected same options.")
    elif user_input == "rock" and Computer_input == "scissors":
        print(f"{Computer_input} vs {user_input}\nYou won!")
        you += 1
    elif user_input == "scissors" and Computer_input == "paper":
        print(f"{Computer_input} vs {user_input}\nYou won!")
        you += 1
    elif user_input == "paper" and Computer_input == "rock":
        print(f"{Computer_input} vs {user_input}\nYou won!")
        you += 1
    else:
        print(f"{Computer_input} vs {user_input}\n Computer won!")
        Computer += 1
print(f"You won the game {you} times against the Computer!\nComputer won the game {Computer} times against the You!")
print("Good Bye!")

"""
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

"""





