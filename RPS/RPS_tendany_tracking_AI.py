import random

play = "y"
userChoice = None

user_rock = 0
user_paper = 0
user_scissors = 0
wins = 0
losses = 0
ties = 0

while play == "y":

    userChoice = None
    while userChoice != "rock" and userChoice != "paper" and userChoice != "scissors":
        userChoice = input("What is your choice? (rock, paper, or scissors) ")
        if userChoice == "rock":
            user_rock += 1
        elif userChoice == "paper":
            user_paper += 1
        elif userChoice == "scissors":
            user_scissors += 1
        else:
            print("Please input rock, paper, or scissors")

    if user_rock > user_paper + 2 or user_rock > user_scissors + 2:
        computerChoice = "paper"
    elif user_paper > user_rock + 2 or user_paper > user_scissors + 2:
        computerChoice = "scissors"
    elif user_scissors > user_paper + 2 or user_scissors > user_rock + 2:
        computerChoice = "rock"
    else:
        computerChoice = random.choice(["rock", "paper", "scissors"])

    if userChoice == computerChoice:
        print(f"I chose {computerChoice}. You chose {userChoice}. It's a tie!")
        ties += 1

    elif computerChoice == "rock":
        if userChoice == "scissors":
            print("Rock beats scissors. I win!")
            losses += 1
        if userChoice == "paper":
            print("Paper beats rock. You win!")
            wins += 1

    elif computerChoice == "paper":
        if userChoice == "scissors":
            print("Scissors beats paper. You win!")
            wins += 1
        if userChoice == "rock":
            print("Paper beats rock. I win!")
            losses += 1

    elif computerChoice == "scissors":
        if userChoice == "rock":
            print("Rock beats scissors. You win!")
            wins += 1
        if userChoice == "paper":
            print("Scissors beats paper. I win!")
            losses += 1

    print(f"\nWins: {wins} Losses: {losses} Ties: {ties}")
    play = input("Do you want to play again? (y/n) ")
    if play == "y" or play == "yes" or play == "Yes" or play == "YES":
        play = "y"
    elif play != "n" or play != "no" or play != "No" or play != "NO":
        print("Thank you for playing!")