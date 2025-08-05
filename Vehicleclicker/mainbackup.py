# Saving system
# more buttons
#more exponential
# look good
# make it work on web

import customtkinter as ctk
import json
import time as t
import tkinter as tk
import threading as thr
# set a buch of vars ready
root = tk.Tk()
root.title("I am a screen")
# saved vars
persecond_thread = False
carnum = 1
car = int
root.geometry("500x500")
money = 0 
num = 1
carman = 1
numps = 0
filepath = "Vehicleclicker/data.json"

##################################################################################
#
# This is for the functions
#


#########################
#Money makers
# function for the main button money
def addmoney():
    global num
    global money
    money += num
    updatedisplay()

# thread for the amount of money per second 
def persecond():
    global numps
    global money 
    while True:
        if numps > 0:
            t.sleep(1)
            money += numps
            updatedisplay()

#buying things

# function for buying management
def managerbuy(what_industry):
    
    global numps 
    global money
    global carman
    global persecond_thread
    if what_industry == "Cars":
        if persecond_thread is not True:
            thr.Thread(target=persecond, daemon=True).start()
            persecond_thread = True
        if money > carman* 15 -1:
            money -= carman* 15
            carman += 1
            numps += 1
            updatedisplay()
            buttoncarman.configure(text= f"🚗 manager\n {carman*15}\n total managers\n {carman-1}")
        else:
            nomoney()

# function for buying vehicles\
def buttonbuy(whatvehicle):
    global num 
    global money
    global carnum
    if whatvehicle == "Car":
        if money > carnum* 15 - 1:
            money -= carnum* 15
            carnum += 1
            num += 1
            updatedisplay()
            buttoncarup.configure(text= f"Car\n {carnum*15}\n total Cars {carnum-1}")
        else:
            nomoney()

###############################
# other functions


datasave ={
    "persecthr ": persecond_thread,
    "amount of cars ": carnum,
    "amount of car managers ": carman,
    "Num per click ": num,
    "num per second ": numps,
    "Money ": money
}
# save function
def saveme():
    with open(filepath, "w") as fw:
        json.dump(datasave, fw)
    

# load functions
def loadme():
    ...

# function to show player that they dont have enough money
def nomoney():
    global money
    moneydisplay.configure(text = "Not enough money", text_color = "red")
    root.after(1000,lambda: moneydisplay.configure(text = f"You have ${money} ", text_color = "black"))
# function to update display
def updatedisplay():
    moneydisplay.configure(text = f"You have ${money}\n You get {num} P.C.\nYou have {numps} P.S.")

#############################################################################################
# This is for creating buttons
#

#Save and load buttons



savebut = ctk.CTkButton(
                master=  root,
                width = 60,
                height= 50,
                text= "Save",
                command=saveme
                
                        )

# for upgrades

upgradesbutt = ctk.CTkButton( root)

#creates the button to buy a car

buttoncarup = ctk.CTkButton(
                        root,
                        corner_radius=15,
                        background_corner_colors=("White","White","White","White",),
                        text= "Car\n 15",
                        width=90,
                        height= 80,
                        command=lambda: buttonbuy("Car"),
                        text_color= "white"                       
)

##creates the button for buying a manager

buttoncarman = ctk.CTkButton(
                        root,
                        corner_radius=15,
                        background_corner_colors=("White","White","White","White",),
                        text= "🚗\nmanagers\n 15",
                        width=90,
                        height= 80,
                        command=lambda: managerbuy("Cars"),
                        text_color= "white"                       
)

# Creates the display of money
moneydisplay = ctk.CTkLabel(
    root,
    width= 200,
    height= 30,
    font=("Arial", 28),
    text= "You are poor",
)


# creates the main button
mainbutton = ctk.CTkButton(
                            root,
                            text ="🚲",
                            width= 150,
                            height= 150,
                            font= ("Arial", 100),
                            command=lambda: addmoney()
)
# placing buttons
mainbutton.place(x = 165, y = 175)
buttoncarman.place(x = 390, y =190)     
moneydisplay.place(x = 125, y = 15)   
buttoncarup.place(x = 390, y = 100)
savebut.place(x = 10, y = 10)
#    buttonlayout = [
 #               [ savebut,  moneydisplay, loadbut],
  #              [ upgrademenu, mainbutton, car_sales ],
  #              [bus_sales, truck_sales,  vans_sales]
  # ]



# shows the screen
root.mainloop()





