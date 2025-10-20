import random as r
options = ["rock","paper","scissors"]


wins = 0
draws = 0
losses = 0
play_again = True
score = 0

user_rock = 1
user_paper = 1
user_scissors = 1

weights = [(user_scissors*10),(user_rock*10),(user_paper*10)]


while(play_again):
    user_choice = input("Enter a choice (rock,paper,scissors): ")

    comp_choice = r.choices(options, weights=weights,k=1)[0]
    print(comp_choice)

    if comp_choice == user_choice:
        draws +=1
        print("draw")
    
    if user_choice== "rock":
        user_rock +=1
        if comp_choice == "scissors":
            wins += 1
        elif comp_choice == "paper":
            losses += 1
    if user_choice== "paper":
        user_paper +=1
        if comp_choice == "rock":
            wins += 1
        elif comp_choice == "scissors":
            losses += 1
    if user_choice== "scissors":
        user_scissors +=1
        if comp_choice == "paper":
            wins += 1
        elif comp_choice == "rock":
            losses += 1
       
    

    score = wins - losses
    print(f"Computer chose {comp_choice}. You chose {user_choice}")
    print(f"Score: {score}")
    user_plays_again = input("Want to play again (y or n): ")

    if user_plays_again== "y":
        play_again = True
    else:
        play_again = False
    
print(f"You won {wins} times!")