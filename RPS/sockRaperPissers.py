import random as randomThingsThatLukeLukeDecidedToTypeWhileNotLukeWasBusyGettingADonutAndWashingHisHandsHEHEHEHEHE
options = ["Rock", "Paper", "Scissors"]
arrayMaker = 0
while(arrayMaker < 70):
    options.append("")
    arrayMaker += 1
options[67] = "GUN"
result = "John"  #    0 = loss, 1 = win, 0.5 = tie. LUKELUKE'sgotahugecrushonCECHOF :O 
yesSlang = ["y", "yes", "nah yeah", "yeah", "sure", "suure", "sure why not", "sure, why not?", "of course", "yep", "ye", "yea", "uh huh", "absolutely", "i guess so", "yes!", "certainly", "obviously", "yess", "yeahh", "okay", "um okay", "why not", "ehh i guess so", "wellllll okay", "yessssssss", "yesssss", "yesssssss", "yessssss", "yessss", "yesss", "yes.", "yes!", "yuh", "mhm", "mhmm", "the opposite of no", "ugh just like go already", "indubitibly", "affirmative", "indubitably"]
noSlang = ["n", "no", "nope", "nah", "nahh", "i don't think so", "yeah nah", "no sir", "negative", "noo", "nooo", "noooo", "nooooo", "nip nap nope", "nuh uh", "of course not", "no thanks", "no thank you", "no, thank you", "how bout no"]
rockSlang = ["rock", "r", "dwayne", "dwayne johnson", "stone", "pebble", "rocky",  "rock!", "rok"]
paperSlang = ["paper", "p", "sheet", "flat white thingy", "modern clay tablet", "scroll"]
scissorsSlang = ["scissors", "s", "snip snip", "cutters", "sharp things"]

humanWins = 0
compWins = 0
draws = 0
playAgain = True

last3HumanChoices = [4, 4, 4]

def displayOutcome(cChoice, hChoice, r, w, l, d):
    print(f"Your choice:  {hChoice}")
    print(f"Comp choice:  {cChoice}\n**********")
    if(r == 0):
        print("You lost.")
    elif(r == 0.5):
        print("You tied.")
    elif(r == 1):
        print("You won!")
    print(f"\n----------\nTOTAL SCORE:\nWins:     {w}\nLosses:   {l}\nDraws:    {d}\n-----------")
#  Will display result of one game and then total score

def askToPlayAgain():
    status = input("Do you wish to play again?  ").lower()
    if(status in yesSlang):
        status = True
    if(status in noSlang):
        status = False
    while(status != True and status != False):
        status = input("I inquire again, in hopes of a clearer answer, do you wish to play again?  ")
        if(status in yesSlang):
            status = True
        if(status in noSlang):
            status = False
    return status
#  Will ask if human wants to play again and return true or false

def assignCompChoice(humanChoices):
    compChoice = randomThingsThatLukeLukeDecidedToTypeWhileNotLukeWasBusyGettingADonutAndWashingHisHandsHEHEHEHEHE.randint(0,2)

    if(humanChoices[0] == humanChoices[1] and humanChoices[1] == humanChoices[2]):
        compChoice = (humanChoices[1] + 1) % 3
    return compChoice
#  Will choose what computer throws

def askHumanChoice():
    humanChoice = input("Choose rock, paper, or scissors:  ")
    if(humanChoice in rockSlang):
        humanChoice = 0
    elif(humanChoice in paperSlang):
        humanChoice = 1
    elif(humanChoice in scissorsSlang):
        humanChoice = 2
    elif(humanChoice == "GUN"):
        humanChoice = 67
    while(humanChoice != 0 and humanChoice != 1 and humanChoice != 2 and humanChoice != 67):
        humanChoice = input("I inquire again, in hopes of a clearer answer, which do you wish to play: rock, paper, or scissors?  ")
        if(humanChoice in rockSlang):
            humanChoice = 0
        elif(humanChoice in paperSlang):
            humanChoice = 1
        elif(humanChoice in scissorsSlang):
            humanChoice = 2
    return humanChoice

while(playAgain):
    compChoice = assignCompChoice(last3HumanChoices)

    humanChoice = askHumanChoice()
    last3HumanChoices[2] = last3HumanChoices[1]
    last3HumanChoices[1] = last3HumanChoices[0]
    last3HumanChoices[0] = humanChoice

    if(humanChoice == 67):
        result = 1
        humanWins += 1
    else:
        if(compChoice == humanChoice):
            result = 0.5
            draws += 1
        elif((humanChoice + 1) % 3 == compChoice):
            result = 0
            compWins += 1
        elif((humanChoice - 1) % 3 == compChoice):
            result = 1
            humanWins += 1


    compChoice = options[compChoice]
    humanChoice = options[humanChoice]


    displayOutcome(compChoice, humanChoice, result, humanWins, compWins, draws)

    playAgain = askToPlayAgain()
