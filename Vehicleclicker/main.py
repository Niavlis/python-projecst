# Saving system
# more buttons
#more exponential
# look good
# make it work on web

from dataclasses import dataclass, asdict
import customtkinter as ctk
import json
import time as t
import tkinter as tk
import threading as thr

root = tk.Tk()
root.title("I am a screen")
root.geometry("500x500")

@dataclass
class Gamesave:
    persecond_thread: bool = False
    carnum: int = 1
    money: int = 0
    num: int = 1
    carman: int = 1
    numps: int = 0

state = Gamesave()
filepath = "Vehicleclicker/data.json"

# Function for the main button money
def addmoney():
    state.money += state.num
    updatedisplay()

# Thread for the amount of money per second 
def persecond():
    while True:
        if state.numps > 0:
            t.sleep(1)
            state.money += state.numps
            updatedisplay()

# Function for buying management
def managerbuy(what_industry):
    if what_industry == "Cars":
        if state.persecond_thread is not True:
            thr.Thread(target=persecond, daemon=True).start()
            state.persecond_thread = True
        if state.money > state.carman * 15 - 1:
            state.money -= state.carman * 15
            state.carman += 1
            state.numps += 1
            updatedisplay()
            buttoncarman.configure(text=f"🚗 manager\n {state.carman * 15}\n total managers\n {state.carman - 1}")
        else:
            nomoney()

# Function for buying vehicles

def buttonbuy(whatvehicle):
    if whatvehicle == "Car":
        if state.money > state.carnum * 15 - 1:
            state.money -= state.carnum * 15
            state.carnum += 1
            state.num += 1
            updatedisplay()
            buttoncarup.configure(text=f"Car\n {state.carnum * 15}\n total Cars {state.carnum - 1}")
        else:
            nomoney()

# Save function
def saveme():
    try:
        with open(filepath, "w") as fw:
            json.dump(asdict(state), fw)
    except TypeError:
        moneydisplay.configure(text="Save File\nis corrupted", text_color="red")
        root.after(1000, lambda: moneydisplay.configure(text=f"You have ${state.money} ", text_color="black"))
    except Exception:
        moneydisplay.configure(text="Save File\nis corrupted", text_color="red")
        root.after(1000, lambda: moneydisplay.configure(text=f"You have ${state.money} ", text_color="black"))
# Load function
def loadme():
    global state
    with open(filepath, "r") as f:
        loaddata = json.load(f)
    state = Gamesave(**loaddata)
    updatedisplay()
    updateall()

# Function to show player that they don't have enough money
def nomoney():
    moneydisplay.configure(text="Not enough money", text_color="red")
    root.after(1000, lambda: moneydisplay.configure(text=f"You have ${state.money} ", text_color="black"))

# Function to update display
def updatedisplay():
    moneydisplay.configure(text=f"You have ${state.money}\n You get {state.num} P.C.\nYou have {state.numps} P.S.")

#update all
def updateall():
    updatedisplay()
    buttoncarup.configure(text=f"Car\n {state.carnum * 15}\n total Cars {state.carnum - 1}")
    buttoncarman.configure(text=f"🚗 manager\n {state.carman * 15}\n total managers\n {state.carman - 1}")

# Save and load buttons
loadbut = ctk.CTkButton(
    master=root,
    width=60,
    height=50,
    text="Load\nlast save",
    command=loadme
)

savebut = ctk.CTkButton(
    master=root,
    width=60,
    height=50,
    text="Save",
    command=saveme
)

# For upgrades
upgradesbutt = ctk.CTkButton(root)

# Creates the button to buy a car
buttoncarup = ctk.CTkButton(
    root,
    corner_radius=15,
    background_corner_colors=("White", "White", "White", "White",),
    text="Car\n 15",
    width=90,
    height=80,
    command=lambda: buttonbuy("Car"),
    text_color="white"
)

# Creates the button for buying a manager
buttoncarman = ctk.CTkButton(
    root,
    corner_radius=15,
    background_corner_colors=("White", "White", "White", "White",),
    text="🚗\nmanagers\n 15",
    width=90,
    height=80,
    command=lambda: managerbuy("Cars"),
    text_color="white"
)

# Creates the display of money
moneydisplay = ctk.CTkLabel(
    root,
    width=200,
    height=30,
    font=("Arial", 28),
    text="You are poor",
)

# Creates the main button
mainbutton = ctk.CTkButton(
    root,
    text="🚲",
    width=150,
    height=150,
    font=("Arial", 100),
    command=lambda: addmoney()
)

# Placing buttons
mainbutton.place(x=165, y=175)
buttoncarman.place(x=390, y=190)
moneydisplay.place(x=125, y=15)
buttoncarup.place(x=390, y=100)
savebut.place(x=10, y=10)
loadbut.place(x=410, y=10)

# Shows the screen
root.mainloop()
