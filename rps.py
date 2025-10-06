import random as r
options = ["rock","paper","scissors"]


wins = 0
draws = 0
losses = 0
play_again = True
score = 0

while(play_again):
    user_choice = input("Enter a choice (rock,paper,scissors): ")

    comp_choice = r.choice(options)

    if comp_choice == user_choice:
        draws +=1
    elif user_choice == "rock" and comp_choice == "paper":
        losses +=1
    elif user_choice == "paper" and comp_choice == "scissors":
        losses +=1
    elif user_choice == "scissors" and comp_choice == "rock":
        losses +=1
    elif user_choice == "rock" and comp_choice == "scissors":
        wins+=1
        print("You won!")
    elif user_choice == "paper" and comp_choice == "rock":
        wins+=1
        print("You won!")
    elif user_choice == "scissors" and comp_choice == "paper":
        wins+=1
        print("You won!")
    else:        
        print("not an option")
    score = wins - losses
    print(f"Computer chose {comp_choice}. You chose {user_choice}")
    print(f"Score: {score}")
    user_plays_again = input("Want to play again (y or n): ")

    if user_plays_again== "y":
        play_again = True
    else:
        play_again = False
    
print(f"You won {wins} times!")
