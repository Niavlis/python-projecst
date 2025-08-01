import tkinter as tk
import customtkinter as ctk
from tkinter import font as tkFont
frame = tk.Tk()
frame.title("Calculator bad")
frame.geometry( "440x440")
frame.config(bg="grey")         
custom_font = tkFont.Font(family="Digital-7", size=20, weight="bold")   
currentinput = tk.StringVar(value="")


root = ctk.CTkFrame( frame, width= 310, height= 370)

root.place(x = 50, y = 50)
display = ctk.CTkEntry(
                     root,
                     width= 270,
                     height=60,
                     justify = "right",
                     font=(custom_font, 28),
                     textvariable = currentinput,
                     border_width= 10,
                     
                     

)



display.place(x = 20, y = 10)
def buttonpress(text):
    if text == "=":
        try:

            currentinput.set(eval(currentinput.get()))
        except Exception:
            currentinput.set("Error")
    elif text == "C":
        currentinput.set("")
        
    
    else:
        currentinput.set(currentinput.get() + text )




button = []
def createbutton(parent, text, x, y, width, height):
    button = ctk.CTkButton(
                        parent,
                        text = text,
                        font=(custom_font, 24),
                        width = width,
                        height = height,
                        text_color = "black",
                        fg_color= "dark green",
                        command=lambda: buttonpress(text)

                        
    ).place(x = x, y = y)


createbutton(root, "*" , 160, 90, 60, 60)
createbutton(root, "C" , 230, 90, 60, 60)
createbutton(root, "-" , 230, 160, 60, 60)
createbutton(root, "+" , 230, 230, 60, 60)
createbutton(root, "/" , 90, 90, 60, 60)
createbutton(root, "=" , 230, 300, 60, 60)
createbutton(root, "0" , 20, 90, 60, 60)
createbutton(root, "9" , 160, 160, 60, 60)
createbutton(root, "8" , 90, 160, 60, 60)
createbutton(root, "7" , 20, 160, 60, 60)
createbutton(root, "6" , 160, 230, 60, 60)
createbutton(root, "5" , 90, 230, 60, 60)
createbutton(root, "4" , 20, 230, 60, 60)
createbutton(root, "3" , 160, 300, 60, 60)
createbutton(root, "2" , 90, 300, 60, 60)
createbutton(root, "1" , 20, 300, 60, 60)



root.mainloop()



# in total took about 5 hours to figure everything out