# a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
#
# number = int(input("Enter a number: "))
#
# new_list = []
# higher_list = []
# for index in a:
#     if index < number:
#         new_list.append(index)
#         print(new_list)
#     elif index > number:
#         higher_list.append(index)
#         print(higher_list)
#     else:
#         print("Invalid input")



# def temperature_c_to_f():
#     celcius = int(input("What is the temperature in Celcius?: "))
#     fahrenheit = 9/5 * celcius + 32
#     print("The temperature is", fahrenheit, "degrees Fahrenheit. ")
#
# temperature_c_to_f()

# def sleep_in(weekday, vacation):
#     if not weekday or vacation:
#         return True
#     else:
#         return False
#
# def string_times(str,n):
#     str * n
#
# def hello_name(name):
#     return "Hello " + name + "!"
#


# import random
# first_name = ["Kevin", "Jim", "Kelcie"]
# last_name = ["Juan", "Hyde", "Kelso"]
#
# name1 = random.choice(first_name)
# name2 = random.choice(last_name)
#
# print(name1, name2)

import random
computer_answers = ["rock", "paper", "scissors"]
player_answers = input("Enter your play: ")

computer = random.choice(computer_answers)
player = player_answers

print(computer)

if player == computer:
    print("Tie")
elif player == "rock" and computer == "scissors":
    print("Player wins")
elif player == "rock" and computer == "paper":
    print("Computer wins")
elif player == "paper" and computer == "scissors":
    print("Computer wins")
elif player == "paper" and computer == "rock":
    print("Player wins")
elif player == "scissors" and computer == "rock":
    print("Computer wins")
elif player == "scissors" and computer == "paper":
    print("Player wins")
elif computer == "rock" and player == "scissors":
    print("Computer wins")
elif computer == "rock" and player == "paper":
    print("Player wins")
elif computer == "paper" and player == "scissors":
    print("Player wins")
elif computer == "paper" and player == "rock":
    print("Computer wins")
elif computer == "scissors" and player == "rock":
    print("Player wins")
elif computer == "scissors" and player == "paper":
    print("Computer wins")
else:
    if player != "rock" or "paper" or "scissors":
        print("Invalid Play")
