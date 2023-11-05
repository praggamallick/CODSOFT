import random

arr = ("rock", "paper", "scissors")

user_input = None
computer_input = random.choice(arr)
user_input = input("Enter a choice (rock, paper, scissors): ")

print("Your input:" ,user_input)
print("Computer's input:" ,computer_input)

if user_input == computer_input:
    print("OOPS!..It's a tie!")
elif user_input == "rock" and computer_input == "scissors":
    print("Congratulations..You win!")
elif user_input == "paper" and computer_input == "rock":
    print("Congratulations..You win!")
elif user_input == "scissors" and computer_input == "paper":
    print("Congratulations..You win!")
else:
    print("OOPS!..You lose!")

print("Thanks for playing!")