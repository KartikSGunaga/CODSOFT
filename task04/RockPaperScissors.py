from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
import random as rd

class PlayRockPaperScissors:
    def __init__(self):
        self.userScore = 0
        self.compScore = 0

    def decideWinner(self, userChoice, compChoice):
        play = ["rock", "paper", "scissors"]
        userIndex = play.index(userChoice)
        compIndex = play.index(compChoice)

        if (userIndex == 2 and compIndex == 1) or (compIndex > userIndex):
            self.compScore += 1
        else:
            self.userScore += 1

    def declareWinner(self):
        if self.userScore == self.compScore:
            return "It's a tie!"
        elif self.userScore > self.compScore:
            return "You won!"
        else:
            return "Computer wins!"

    def viewScores(self):
        return f"Computer Score: {self.compScore}\nUser score: {self.userScore}."


class RockPaperScissorsApp(App):
    def build(self):
        self.players = PlayRockPaperScissors()
        self.layout = BoxLayout(orientation='vertical')

        # Widgets
        self.label = Label(text="Welcome to the Rock-Paper-Scissors Game!", size_hint=(1, 0.1))
        self.layout.add_widget(self.label)

        # TextInput for user choice
        self.user_input = TextInput(hint_text="Enter your choice (rock/paper/scissors)")
        self.layout.add_widget(self.user_input)

        # Buttons
        self.buttons = [
            Button(text="Play Game", on_press=self.playGame),
            Button(text="View Scores", on_press=self.viewScores),
            Button(text="Exit", on_press=self.exitApp)
        ]

        for button in self.buttons:
            self.layout.add_widget(button)

        return self.layout

    def playGame(self, instance):
        userChoice = self.user_input.text.lower()

        if userChoice not in ["rock", "paper", "scissors"]:
            self.label.text = "Invalid choice. Please enter rock, paper, or scissors."
            return

        compChoice = rd.choice(["rock", "paper", "scissors"])

        self.players.decideWinner(userChoice, compChoice)

        result_label = Label(text=f"User Choice: {userChoice}\nComp Choice: {compChoice}\n{self.players.declareWinner()}")
        self.layout.add_widget(result_label)

    def viewScores(self, instance):
        scores_label = Label(text=self.players.viewScores())
        self.layout.add_widget(scores_label)

    def exitApp(self, instance):
        self.stop()


if __name__ == "__main__":
    RockPaperScissorsApp().run()
