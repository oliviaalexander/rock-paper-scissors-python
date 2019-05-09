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
