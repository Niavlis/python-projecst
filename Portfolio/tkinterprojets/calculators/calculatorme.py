import tkinter as tk
import customtkinter as ctk

frame = tk.Tk()
frame.title("Calculator bad")
frame.geometry( "500x500")


currentinput = tk.StringVar(value="")


root = ctk.CTkFrame( frame, width= 350, height= 350)

root.place(x = 50, y = 50)
display = ctk.CTkEntry(
                     root,
                     width= 270,
                     height=60,
                     justify = "right",
                     font=('Arial', 28),
                     textvariable = currentinput                             
)



display.place(x = 20, y = 10)
def buttonpress(text):
    print(f"you pressed {text}")
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
                        font=('Arial', 24),
                        width = width,
                        height = height,
                        text_color = "black",
                        fg_color= "dark green",
                        command=lambda: buttonpress(text)

                        
    ).place(x = x, y = y)


createbutton(root, "*" , 20, 90, 60, 60)
createbutton(root, "C" , 260, 190, 60, 60)
createbutton(root, "-" , 260, 260, 60, 60)
createbutton(root, "+" , 260, 330, 60, 60)
createbutton(root, "/" , 120, 190, 60, 60)
createbutton(root, "=" , 260, 400, 60, 60)
createbutton(root, "0" , 50, 190, 60, 60)
createbutton(root, "9" , 190, 260, 60, 60)
createbutton(root, "8" , 120, 260, 60, 60)
createbutton(root, "7" , 50, 260, 60, 60)
createbutton(root, "6" , 190, 330, 60, 60)
createbutton(root, "5" , 120, 330, 60, 60)
createbutton(root, "4" , 50, 330, 60, 60)
createbutton(root, "3" , 190, 400, 60, 60)
createbutton(root, "2" , 120, 400, 60, 60)
createbutton(root, "1" , 50, 400, 60, 60)



root.mainloop()
