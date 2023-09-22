import tkinter as tk
import numpy as np
import matplotlib.pyplot as plt
import math
from PIL import Image, ImageTk
from random import *
import time

'''
xvalues = np.array([0,1,2,3])
yvalues = np.array([12,32,42,52])


plt.scatter(xvalues, yvalues, label='Points', color = 'green', marker = 'o')

plt.ylabel('some numbers')

plt.savefig('DiagrammeTest.png')
'''
'''
def f ( x ) :
    return x **2 + x *3 + 2



def plot_fct(fonction, x1, x2):
    xValues = np.linspace(x1, x2, 100)
    yValues = []
    for x in xValues:
        y = fonction(x)
        yValues.append(y)
    plt.plot(xValues,yValues)

    plt.xlabel('x')
    plt.ylabel('f(x)')

    plt.grid(True)

    plt.savefig('DiagrammeTest.png')
    Image.open('DiagrammeTest.png').show()



#plot_fct ( math.sin , 0 , 50)
#plot_fct (f , -100 , 200)
#plot_fct ( lambda x : x **2 , -10 , 10)
#plot_fct ( lambda x : 1/ x , -100 , 100)
'''
'''
def convertToUppercase():
    inputText = entry.get()
    upperText = inputText.upper()
    print(upperText)

root = tk.Tk()
root.title('Tkinter Test')

backgroundImage = Image.open('ImageTestArbre.jpg')
backgroundImagePhoto = ImageTk.PhotoImage(backgroundImage)

canvas = tk.Canvas(root, width=backgroundImage.width, height=backgroundImage.height)
canvas.pack()
canvas.create_image(0, 0, anchor=tk.NW, image= backgroundImagePhoto)

label = tk.Label(root, text='image sympa')
label.pack()

labelFrame = tk.LabelFrame(root, text="Label Frame")
labelFrame.pack(padx=10, pady=10)

entry=tk.Entry(labelFrame)
entry.pack(padx=10, pady=10)

convertButton = tk.Button(labelFrame, text="Convert to Uppercase", command=convertToUppercase)
convertButton.pack(padx=10, pady=10)


root.mainloop()
'''
'''
'''
def dessinerStickman():
    canvas.delete("all")
    canvas.create_oval(175, 20, 225, 70, fill="green")
    canvas.create_line(200,70,200,150, fill="darkgreen")
    canvas.create_line(200,70,randint(100,150),randint(10,150), fill="red")
    canvas.create_line(200,70,randint(250,300),randint(10,150), fill="blue")
    canvas.create_line(200,150,randint(110,195),200, fill="purple")
    canvas.create_line(200,150,randint(205,290),200, fill="orange")
    text()

def text():
    canvas.create_text(100, 10, text="Hello World", font=("Arial", 16), fill="black")
    
# Fonction pour dessiner un cercle
def dessinerCercle():
    canvas.create_oval(175, 20, 225, 70, fill="green")

# Fonction pour dessiner un rectangle
def dessinerRectangle():
    canvas.create_rectangle(100, 50, 300, 150, fill="darkgreen")

def dessinerLigne():
    canvas.create_line(200,70,200,200)

# Fonction pour effacer tout le dessin
def effacer_dessin():
    canvas.delete("all")

# Créer une fenêtre tkinter
root = tk.Tk()
root.title("Dessin avec tkinter")

# Créer un widget Canvas pour le dessin
canvas = tk.Canvas(root, width=400, height=200)
canvas.pack()

# Créer des boutons pour dessiner un cercle, un rectangle et effacer
#button_cercle = tk.Button(root, text="Dessiner Cercle", command=dessinerCercle)
#button_rectangle = tk.Button(root, text="Dessiner Rectangle", command=dessinerRectangle)
button_Stickman = tk.Button(root, text='Dessiner Stickman', command=dessinerStickman)
button_effacer = tk.Button(root, text="Effacer Dessin", command=effacer_dessin)

#button_cercle.pack()
#button_rectangle.pack()
button_Stickman.pack()
button_effacer.pack()

# Démarrer la boucle principale tkinter
root.mainloop()
'''

def liveScore(time):
    currentScore = (x for x in range(0, 1000000, 10)) 
    canvas.create_text(500, 10, text=currentScore, font=("Arial", 10), fill="black")
    timecount(time)
    

def timecount(currentTime):
    canvas.create_text(100, 10, text=currentTime, font=("Arial", 10), fill="black")
    lifeBar()
    
def lifeBar():
    canvas.create_polygon(175, 250, 100, 150, 250, 150, fill="red")
    canvas.create_arc(100,100,180,200, start=0, extent=180, fill="red", outline="red")
    canvas.create_arc(170,100,250,200, start=0, extent= 180, fill="red", outline="red")

def inventory():
    canvas.create_rectangle()

root = tk.Tk()
root.title("GUI")

canvas = tk.Canvas(root, width=1000, height=1000)
canvas.pack()

current_time = int(time.time())
game_time = int(time.time()) - current_time
gameButton = tk.Button(root, text="Start Game", command=liveScore(game_time))

gameButton.pack()

root.mainloop()
'''