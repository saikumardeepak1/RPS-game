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

Creating a Branch

"""
