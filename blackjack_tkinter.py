"""
Kyle Ruiz
CIS 202 - Python
2/10/2021
"""

from tkinter import *
import random

root = Tk()
root.title("Black Jack")
root.tk_setPalette("black")

playerHand = []
dealerHand = []

playerScore = 0
dealerScore = 0
playerNumCards = 0
dealerNumCards = 0
playerGameScore = 0
dealerGameScore = 0

playerHasHardAce = False
dealerHasHardAce = False
roundOver = False

def update():
    global playerScore
    global dealerScore
    global playerNumCards
    global dealerNumCards
    global playerHasHardAce
    global dealerHasHardAce

    playerScore = 0
    dealerScore = 0
    playerNumCards = 0
    dealerNumCards = 0
    playerHasHardAce = False
    dealerHasHardAce = False

    for i in range(len(playerHand)):
        playerNumCards += 1
        if playerHand[i] == 1 and playerScore <= 11:
            playerHasHardAce = True
            playerScore += 10
        playerScore += playerHand[i]

    if playerScore >= 22 and playerHasHardAce:
        playerScore -= 10
        playerHasHardAce = False

    for i in range(len(dealerHand)):
        dealerNumCards += 1
        if dealerHand[i] == 1 and dealerScore <= 11:
            dealerHasHardAce = True
            dealerScore += 10
        dealerScore += dealerHand[i]

    if dealerScore >= 22 and dealerHasHardAce:
        dealerScore -= 10
        dealerHasHardAce = False

def dealCards(hand):
    randomCard = random.randint(1, 10)
    hand.append(randomCard)
    update()

def formatCards(hand, turn, who):
    formattedText = ""
    if who == "dealer" and turn == "playerTurn":
        for i in range(len(hand)):
            if i == 0:
                if hand[i] == 1:
                    formattedText += "Ace"
                elif hand[i] == 10:
                    formattedText += "Face Card"
                else:
                    formattedText += str(hand[i])
        return formattedText + ", [HIDDEN]\n"
    else:
        for i in range(len(hand)):
            if i == 0:
                if hand[i] == 1:
                    formattedText += "Ace"
                elif hand[i] == 10:
                    formattedText += "Face Card"
                else:
                    formattedText += str(hand[i])
            else:
                if hand[i] == 1:
                    formattedText += ", " + "Ace"
                elif hand[i] == 10:
                    formattedText += ", " + "Face Card"
                else:
                    formattedText += ", " + str(hand[i])
        return formattedText + "\n"


def hitButtonClicked():
    global roundOver
    dealCards(playerHand)
    playerCardLabel.config(text=formatCards(playerHand, "playerTurn", "player"))
    playerScoreLabel.config(text="Player Score: "+str(playerScore)+"\n" + "—"*10)
    if playerScore >= 22:
        roundOver = True
        roundEval(roundOver, "Dealer")
    elif playerNumCards >= 5 and playerScore < 22:
        roundOver = True
        roundEval(roundOver, "Player")

def standButtonClicked():
    global roundOver
    while dealerScore <= 15:
        dealCards(dealerHand)
    dealerScoreLabel.config(text="\nDealer Score: "+str(dealerScore)+"\n"+"—" * 10)
    dealerCardLabel.config(text=formatCards(dealerHand, "dealerTurn", "dealer"))
    if dealerScore >= 22:
        roundOver = True
        roundEval(roundOver, "Player")
    elif dealerNumCards == 5 and dealerScore < 22:
        roundOver = True
        roundEval(roundOver, "Player")
    else:
        if playerScore > dealerScore:
            roundOver = True
            roundEval(roundOver, "Player")
        else:
            roundOver = True
            roundEval(roundOver, "Dealer")


def dealButtonClicked():
    global roundOver
    global playerHand
    global dealerHand

    playerHand.clear()
    dealerHand.clear()
    roundOver = False

    dealCards(playerHand)
    dealCards(playerHand)
    dealCards(dealerHand)
    dealCards(dealerHand)

    messageLabel.config(text="")
    playerCardLabel.config(text=formatCards(playerHand, "playerTurn", "player"))
    playerScoreLabel.config(text="Player Score: "+str(playerScore)+"\n" + "—"*10)
    dealerCardLabel.config(text=formatCards(dealerHand, "playerTurn", "dealer"))
    dealerScoreLabel.config(text="\nDealer Score: "+str(dealerHand[0])+"\n"+"—" * 10)
    messageLabel.config(text="\n" + "|" + "—"*24 + "|")
    roundEval(roundOver, "none")


def roundEval(isRoundOver, whoWon):
    global playerGameScore
    global dealerGameScore

    if isRoundOver:
        hitButton.config(state=DISABLED)
        standButton.config(state=DISABLED)
        dealButton.config(state=NORMAL)
    else:
        hitButton.config(state=NORMAL)
        standButton.config(state=NORMAL)
        dealButton.config(state=DISABLED)

    if whoWon == "Player":
        playerGameScore += 10
        dealerGameScore -= 10
        messageLabel.config(text="\n" + "|" + "—" * 8 + "[ Player WINS! ]" + "—" * 8 + "|")
    elif whoWon == "Dealer":
        playerGameScore -= 10
        dealerGameScore += 10
        messageLabel.config(text="\n" + "|" + "—" * 8 + "[ Dealer WINS! ]" + "—" * 8 + "|")
    else:
        pass

    if playerGameScore == 0 and dealerGameScore == 0:
        gameScoreLabel.config(text="|"+"—"*9+"[ P "+str(playerGameScore)+" : D "+str(dealerGameScore)+" ]"+"—"*9+"|\n")
    else:
        gameScoreLabel.config(text="|" + "—" * 8 + "[ P " + str(playerGameScore) + " : D " + str(dealerGameScore) + " ]" + "—" * 8 + "|\n")


dealCards(playerHand)
dealCards(playerHand)
dealCards(dealerHand)
dealCards(dealerHand)

buttonFrame = Frame(root)
gameScoreLabel = Label(root, text="|"+"-"*8+"[ P "+str(playerGameScore)+" : D "+str(dealerGameScore)+" ]"+"—"*8+"|\n", padx=10, pady=5, fg="white", font=("Arial Black", 18))
playerScoreLabel = Label(root, text="Player Score: "+str(playerScore)+"\n" + "—"*10, fg="white", font=("Arial Black", 18))
playerCardLabel = Label(root, text=formatCards(playerHand, "playerTurn", "player"), fg="white", font=("Arial Black", 18))
dealerScoreLabel = Label(root, text="\nDealer Score: "+str(dealerHand[0])+"\n"+"—" * 10, fg="white", font=("Arial Black", 18))
dealerCardLabel = Label(root, text=formatCards(dealerHand, "playerTurn", "dealer"), fg="white", font=("Arial Black", 18))
hitButton = Button(buttonFrame, text="Hit", font=("Arial Black", 18), command=hitButtonClicked, width=12, height=0)
standButton = Button(buttonFrame, text="Stand", font=("Arial Black", 18), command=standButtonClicked, width=12, height=0)
dealButton = Button(buttonFrame, text="Deal", font=("Arial Black", 18), command=dealButtonClicked, width=12, height=0)
messageLabel = Label(root, text="\n" + "|" + "—"*24 + "|", fg="white", font=("Arial Black", 18))

gameScoreLabel.grid(row=0, column=0)
playerScoreLabel.grid(row=1, column=0)
playerCardLabel.grid(row=2, column=0)
dealerScoreLabel.grid(row=3, column=0)
dealerCardLabel.grid(row=4, column=0)
buttonFrame.grid(row=6, column=0, sticky="nsew")
messageLabel.grid(row=7, column=0)
hitButton.pack(side=LEFT)
standButton.pack(side=LEFT)
dealButton.pack(side=LEFT)

roundEval(roundOver, "none")

root.mainloop()
