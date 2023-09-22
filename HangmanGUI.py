import tkinter as tk
from random import choice
from PIL import Image, ImageTk

words = ["ordinateur", "systeme", "python", "computer"]

def chooseWord(liste):
    return choice(liste)

def init():
    word = choice(words)
    i = 0
    hidden = ""
    while i < len(word):
        hidden += "_"
        i+=1

def displayWordOnCanvas(word):
    defaultx = 250
    defaulty = 950
    count = 0
    newWord = ""
    for i in range(0, len(word)):
        if(word[i] == "_"):
            newWord += "_"
        else:
            newWord += word[i]
        count += 50
        print(newWord)
    canvas.create_text(defaultx + count, defaulty, text=newWord, font=("Arial, 25"), fill="black")
    

def letterClick(nouvelle_lettre):
    global lettre
    lettre = nouvelle_lettre
    print(lettre)
    isLetterInWord(word, lettre)

def isLetterInWord(word,lettre):
    newWord = ""
    for i in range(0,len(word)):
        if lettre == word[i]:
            newWord += lettre
            print("La lettre est dans le mot")
        else:
            newWord += "_"
    displayWordOnCanvas(newWord)




root = tk.Tk()
root.title("Hangman Game")

backgroundImage = Image.open('Hangman.jpg')
backgroundImagePhoto = ImageTk.PhotoImage(backgroundImage)

canvas = tk.Canvas(root, width=backgroundImage.width, height=backgroundImage.height)
canvas.pack()
canvas.create_image(0, 0, anchor=tk.NW, image=backgroundImagePhoto)

for letter in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
    letter_button = tk.Button(root, text=letter, command=lambda l=letter: letterClick(l))
    letter_button.pack(side=tk.LEFT, padx=5, pady=5)



def main():
    displayWordOnCanvas(hidden)
    letterClick

    

main()

root.mainloop()
