import random as rand

print("Welcome to Stone, Sheet, and Clippers!")
print("Choice 'r', 'p', 's' for rock, paper, and scissors respectively when it is your turn.\n")

choices = ["r","p","s"]
pl_choices = []
game_num = 0
#player choices
pl_r = 0
pl_p = 0
pl_s = 0
#bot choices
ai_r = 0
ai_p = 0
ai_s = 0
# Info
tie = 0
win = 0
lose = 0

def game_loop():
    player_choice = input("(r/p/s): ")
    ai_choice = ""
    global pl_r
    global choices
    global pl_choices
    global game_num
    #player choices
    global pl_r
    global pl_p
    global pl_s
    #bot choices
    global ai_r
    global ai_p
    global ai_s
    # Info
    global tie
    global win
    global lose

    # AI Choice
    
    if player_choice == "r":
        pl_r += 1
        pl_choices.append("r")
    elif player_choice == "p":
        pl_p += 1
        pl_choices.append("p")
    elif player_choice == "s":
        pl_s += 1
        pl_choices.append("s")

    if len(pl_choices) >= 2:
        if pl_choices[game_num] == pl_choices[game_num-1] == "r":
            ai_choice = "p"
        elif pl_choices[game_num] == pl_choices[game_num-1] == "p":
            ai_choice = "s"
        elif pl_choices[game_num] == pl_choices[game_num-1] == "s":
            ai_choice = "r"
        else:
            ai_choice = rand.choice(choices)
    else:
        ai_choice = rand.choice(choices)

    if ai_choice == "r":
        print("AI chose Rock")
        ai_r += 1
    elif ai_choice == "p":
        print("AI chose Paper")
        ai_p += 1
    elif ai_choice == "s":
        print("AI chose Scissors")
        ai_s += 1

    #Win Lose Code
    if player_choice == ai_choice:
        print("Tie!")
        tie += 1
    elif player_choice == "r" and ai_choice == "p":
        print("Lose!")
        lose += 1
    elif player_choice == "p" and ai_choice == "s":
        print("Lose!")
        lose += 1
    elif player_choice == "s" and ai_choice == "r":
        print("Lose!")
        lose += 1
    elif player_choice == "r" and ai_choice == "s":
        print("Win!")
        win += 1
    elif player_choice == "p" and ai_choice == "r":
        print("Win!")
        win += 1
    elif player_choice == "s" and ai_choice == "p":
        print("Win!")
        win += 1
    else:
        print("TextError: Please input correct letter")
    print(f"Wins: {win}, Losses: {lose}, Ties: {tie}\n")
    game_num += 1
    play_again = input("Play Again? (y/n): ")
    if play_again == "y":
        game_loop()

game_loop()
