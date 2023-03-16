print("Welcome to Computer quiz")

playing = input("Do you want to play the game? ")
question_number = 0
def confiramtion(x):

    if x.lower() != "yes" :
        print("Wow")
    else:
        print("Okay!!!!!!!!!!, Let's play :)")
        global question_number
        answer = input("What is the capital of Telangana? ").lower()
        if answer == "hyderabad":
            print("Yes, that's correct!")
            question_number += 1

        answer = input("What is the quickest animal? ").lower()
        if answer == "eagle":
            print("Yay!!, that's correct")
            question_number += 1

confiramtion(playing)

print(f"Congratulations!! you got {question_number} questions correct")

"""
The given code is a simple computer quiz program that asks the user a series of questions and 
checks whether their answers are correct.

The program starts by printing a welcome message and asking the user whether they want to play 
the game. The input from the user is stored in the playing variable. The program then defines 
a function confirmation() that takes the user's input as an argument and checks if the user has 
responded with "yes" or not. If the user did not respond with "yes", the function will print "Wow". 
If the user has responded with "yes", the function will prompt the user with two questions and check 
their answers.

The questions are hard-coded in the function, and the user's input is converted to lowercase 
before checking the answers. If the user's answer is correct, the program prints a congratulatory 
message and increments the question_number variable. After the questions have been answered, the 
function ends, and the program proceeds to call the confirmation() function, passing in the playing 
variable as an argument.

After the confirmation() function is executed, the program prints a message congratulating the 
user on the number of questions they answered correctly, which is stored in the question_number variable.

The given code is a simple beginner-level project, as it only asks two questions and checks for correctness. 
However, it can be expanded by adding more questions and increasing the complexity of the quiz.

"""