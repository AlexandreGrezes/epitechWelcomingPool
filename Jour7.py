from random import *
import argparse
import tkinter as tk
from PIL import Image, ImageTk

class Pendu:
    def start(self, word):
        self.word = word
        self.points = 0
        self.letters = ""
        self.displayWord = ""
        for _ in word:
            self.displayWord += "_ "

    def guessLetter(self, letter):
        if letter in self.letters:
            return "Letter already guessed."
        self.letters += letter

        if letter in self.word:
            tempDisplay = ""
            for i in range(len(self.word)):
                if self.word[i] == letter:
                    tempDisplay += letter + " "
                else:
                    tempDisplay += self.displayWord[i * 2] + " "
            self.displayWord = tempDisplay.strip()
        else:
            self.points += 1

    def gameOver(self):
        return "_" not in self.displayWord

    def display(self):
        pointDisplay = f"/ {self.points} point" if self.points == 1 else f"/ {self.points} points"
        print(self.displayWord + pointDisplay)

def loadWord(filename):
    with open(filename, "r") as file:
        words = [line.strip() for line in file]
    return words

def main(filename):
    liste = loadWord(filename)
    chosenWord = choice(liste)
    game = Pendu()
    game.start(chosenWord)
    score = 0
    bestScore = 20

    while not game.gameOver():
        game.display()
        score += 1
        a = input("Enter a letter or guess the word: ")
        if len(a) == 1:
            game.guessLetter(a)
        else:
            if a.upper() == chosenWord.upper():
                print("Well done! You guessed it was:", chosenWord)
                if score < bestScore:
                    print("Congratulations, you are the new record holder with", score, "attempts")
                    bestScore = score
                else:
                    print("Unfortunately you've made it in ", score, "attempts. The record is", bestScore, "attempts.")
                break

    if game.gameOver():
        if score < bestScore:
            print("Congratulations, you are the new record holder with", score, "attempts")
            bestScore = score
        else:
            print("Unfortunately you've made it in ", score, "attempts. The record is", bestScore, "attempts.")

parser = argparse.ArgumentParser(description="Pendu")
parser.add_argument("filename", help="Name of the file")

args = parser.parse_args()
main(args.filename)

