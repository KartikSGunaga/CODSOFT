import random as rd

def convertNumIntoPlay(num):
    if num == 1:
        return "Rock"
    elif num == 2:
        return "Paper"
    else:
        return "Scissors"
def convertPlayIntoNum(play):
    if play == "r":
        return 1
    elif play == 'p':
        return 2
    else:
        return 3

def displayWinner(compScore, userScore):
    if compScore == userScore:
        print(f"It's a tie! ")
        print(f"CompScore: {compScore}; UserScore: {userScore}")
    elif compScore > userScore:
        print(f"Computer wins!")
        print(f"CompScore: {compScore}; UserScore: {userScore}")
    else:
        print(f"You win!")
        print(f"CompScore: {compScore}; UserScore: {userScore}")

def didUserWin(compChoice, userChoice):
    if ((compChoice == 3) and (userChoice == 1)) or (compChoice > userChoice):
        return False
    elif compChoice == userChoice:
        return None
    else:
        return True

def playTheGame():
    userScore = 0
    compScore = 0

    for i in range(3):
        while True:
            userInput = input("Press 'r' for Rock; 'p' for paper; 's' for scissors: ").lower()

            if userInput in ['r', 'p', 's']:
                break
            else:
                print("Invalid play.")

        compChoice = rd.randrange(1, 4)
        userChoice = convertPlayIntoNum(userInput)

        userWins = didUserWin(compChoice, userChoice)

        if userWins is None:
            # It's a tie, no need to update scores
            pass
        elif userWins:
            userScore += 1
        else:
            compScore += 1

        print()
        print(f"Your play: {convertNumIntoPlay(userChoice)}")
        print(f"Computer's play: {convertNumIntoPlay(compChoice)}")
        print()

    displayWinner(compScore, userScore)

flag = True
while flag:
    print()
    playAgain = input("Press 'y' to play the game; other keys to exit: ")
    if playAgain == "y":
        playTheGame()
        flag = True
    else:
        flag = False