
import random as r
movesPossible = (2,0,1)
# rock, paper, scissors
playerMovesList = [0,1,2]
# win, tie, loss
score = [0,0,0]

def convertPlayerInput(playerInput):
    if playerInput == "rock" or playerInput == "r":
        return 0
    elif playerInput == "paper" or playerInput == "p":
        return 1
    elif playerInput == "scissors" or playerInput == "s":
        return 2
    else:
        playerInput = input("Enter: Rock, Paper, or Scissors please!").lower()
        convertPlayerInput(playerInput)

def rpsGame():
    playerMove = convertPlayerInput(input("Rock, Paper, or Scissors? ").lower())
    robotMove = r.choice(playerMovesList[len(playerMovesList)-2:len(playerMovesList)])
    playerMovesList.append(movesPossible[playerMove])
    if robotMove == movesPossible[playerMove]:
        score[2] += 1
        print("You Lost!!!")
    elif robotMove == playerMove:
        score[1] += 1
        print("You Tied!!!")
    else:
        score[0] += 1
        print("You Win!!")
    print(f"Wins: {score[0]} | Ties: {score[1]} | Losses: {score[2]}")

for i in range(10):
    rpsGame()
    