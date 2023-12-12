import random as rd

play = ["rock", "paper", "scissors"]
# class Choice:
#     def __init__(self, userChoice, compChoice):
#         self.userChoice = userChoice
#         self.compChoice = compChoice

class playRockPaperScissors():
    def __init__(self):
        self.userScore = 0
        self.compScore = 0

    def decideWinner(self, userChoice, compChoice):
        userIndex = play.index(userChoice)
        compIndex = play.index(compChoice)

        if (userIndex == 2 and compIndex == 1) or (compIndex > userIndex):
            self.compScore += 1
        else:
            self.userScore += 1

        print(f"\nUserChoice: {userChoice} \n"
              f"CompChoice: {compChoice}")
        print(f"\nUserScore: {self.userScore} \n"
              f"CompScore: {self.compScore}")

    def declareWinner(self):
        if self.userScore == self.compScore:
            print("\nIt's a tie! ")
        elif self.userScore > self.compScore:
            print("\nYou won! ")
        else:
            print("\nComputer wins!")

    def viewScores(self):
        print(f"\nComputer Score: {self.compScore}\n"
              f"User score: {self.userScore}.")

def Input():
    userChoice = input("Enter your play(\"rock\", \"paper\", \"scissors\"): ").lower()
    compChoice = rd.choice(["rock", "paper", "scissors"])

    return userChoice, compChoice

def main():
    print("\nWelcome to the game Rock-Paper-Scissors! ")
    players = playRockPaperScissors()

    print(" Menu: \n"
          "1. Exit \n"
          "2. Play the Game\n"
          "3. View Scores")

    while True:
        response = int(input("\nEnter your choice:(1-3): "))

        if response == 1:
            print("\nThank you for playing! ")
            break

        elif response == 2:
            for i in range(3):
                userChoice, compChoice = Input()
                players.decideWinner(userChoice, compChoice)
            players.declareWinner()

        elif response == 3:
            players.viewScores()

        else:
            print("Invalid entry. \n"
                  "Please enter numbers within 1-3 only")

if __name__ == "__main__":
    main()


