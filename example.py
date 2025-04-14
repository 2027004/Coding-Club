name = input("What is your name: ")
print(f"hello {name}")

day = input("How is your day?")

print("Hello world")

print("Finn")

print(f"I am so glad you are feeling {day}")
print("Luke Blase")
print("Good job in the musical Luke!")

import random
yourList = ["rock", "paper", "scissors"]
play = ("y")
cluck = 0
while play == ("y"):
    hand = input("choose one, rock, paper, or scissors ")
    random.shuffle(yourList)

    while hand == ("scissors"):

        if yourList[1] == "rock":
            print("lose")
            play = input("do you want to play again y/n ")
            hand = ("choose one, rock, paper, or scissors ")
        if yourList[1] == "paper":
            print("win")
            cluck = cluck + 1
            play = input("do you want to play again y/n ")
            hand = ("choose one, rock, paper, or scissors ")
        if yourList[1] == "scissors":
            print("tie")
            play = input("do you want to play again y/n ")
            hand = ("choose one, rock, paper, or scissors ")

    while hand == "rock":
        if yourList[1] == "rock":
            print("tie")
            play = input("do you want to play again y/n ")
            hand = ("choose one, rock, paper, or scissors ")
        if yourList[1] == "paper":
            print("lose")
            play = input("do you want to play again y/n ")
            hand = ("choose one, rock, paper, or scissors ")
        if yourList[1] == "scissors":
            print("win")
            cluck = cluck + 1
            play = input("do you want to play again y/n ")
            hand = ("choose one, rock, paper, or scissors ")
    while hand == ("paper"):
        
        if yourList[1] == "rock":
            print("win")
            cluck = cluck + 1
            play = input("do you want to play again y/n ")
            hand = ("choose one, rock, paper, or scissors ")
        if yourList[1] == "paper":
            print("tie")
            play = input("do you want to play again y/n ")
            hand = ("choose one, rock, paper, or scissors ")
        if yourList[1] == "scissors":
            print("lose")
            play = input("do you want to play again y/n ")
            hand = ("choose one, rock, paper, or scissors ")

print(f"your score was {cluck}")
