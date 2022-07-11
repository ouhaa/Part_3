import tkinter as tk
from tkinter import ttk
import threading
from random import random, randint
from time import sleep
from random import randint


root = tk.Tk() # On crée la fenêtre.
root.title("Robots") # On lui donne un titre.
root.iconname("Robots") # On lui donne un titre.
root.resizable(False, False) # On l'empêche d'être redimensionnée.

button = tk.Button(root, text="Lancer", command=lambda: Canvas())
button.pack(side=tk.BOTTOM)


Agents = []
devils = []

def createAgents(quantité, type, canvas):
    for i in range(quantité):
        position_x, position_y = randint(0, 300), randint(0, 300)
        if type == "Devil":
            devils.append(canvas.create_oval(position_x, position_y, position_x+20, position_y+20, fill="yellow"))



def Canvas():
    global Agents

    canvas = tk.Canvas(root, width=500, height=500, bg="grey")
    canvas.pack(side=tk.RIGHT)

    global water
    water = canvas.create_oval(300, 300, 10+50, 10+200, fill="blue")
    Agents.append(water)

    devil = canvas.create_oval(0, 0, 10, 10, fill="yellow")
    Agents.append(devil)
    devils.append(devil)
    createAgents(10, "Devil", canvas)


    print(Agents)

    for devil in devils:
        thread = threading.Thread(target = MoveDevil, args = (canvas, devil, 5, 5))
        thread.daemon = True
        thread.start()

def MoveDevil(canvas, devil, local_x_speed, local_y_speed):
    thirst = False
    while True:
        (leftPos, topPos, rightPos, bottomPos) = canvas.coords(devil)

        if leftPos <= 0 or rightPos >= 500:
            local_x_speed = -local_x_speed
        if topPos <= 0 or bottomPos >= 500:
            local_y_speed = -local_y_speed

        if random() <= 0.01:
            thirst = ThirstyDevil(canvas,devil)

        if thirst:
            overlapping_agents = canvas.find_overlapping(leftPos,topPos,rightPos,bottomPos)
            for overlapping_agent in overlapping_agents:
                if overlapping_agent == water:
                    thirst = False
                    canvas.itemconfig(devil, fill="yellow")


        canvas.move(devil, local_x_speed, local_y_speed)



        sleep(0.02)


  # createAgents(10, "Devil", canvas)


print(Agents)
def ThirstyDevil(canvas, devil):
    canvas.itemconfig(devil, fill="orange")
    return True


root.mainloop() # On démarre la fenêtre.
print("Fenêtre fermée.")