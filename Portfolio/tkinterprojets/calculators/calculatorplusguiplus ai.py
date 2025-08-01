import customtkinter as ctk
import tkinter as tk
#creates the base root
root = tk.Tk()
root.geometry("300x420")
root.title("CustomTkinter Calculator")

# creates the var for the input
current_input = tk.StringVar(value="")

# === DISPLAY ===
display = ctk.CTkEntry( # Ctkentry is the box with numbers
    root, # place
    textvariable=current_input,# this is 
    font=("Arial", 24),     # font
    justify="right", # side where to write
    height=60,         # panel dimensions and other info
    width=260,
    corner_radius=10,
    fg_color="white",
    text_color="black"
)
display.place(x=20, y=20)       # where the panel gets placed


def button_pressed(value):  # function of the button which gets pressed
    if value == "C":    # checks for Clear input and clears screen
        current_input.set("")
    elif value == "=":      # checks for the result function
        try:
            result = str(eval(current_input.get()))     # it checks the input and calculates
            current_input.set(result)           # puts the input as result
        except Exception:                   #if not poosible to calculate  show error
            current_input.set("Error")
    else:
        current_input.set(current_input.get() + str(value))         # if not 1 of the C or = throw it on current inpu

# === BUTTON CREATION FUNCTION ===          
def createbutton(parent, text, x, y):           #definition to create the buttons
    btn = ctk.CTkButton(
        parent,
        text=str(text),
        font=('Arial', 20),
        command=lambda: button_pressed(text),
        bg_color="PeachPuff3",
        fg_color="PeachPuff1",
        text_color="Snow4",
        corner_radius=15,
        hover_color="PeachPuff2",
        height=60,
        width=60,
    )
    btn.place(x=x, y=y)
    return btn

# === BUTTON LAYOUT DATA ===
button_values = [           # data on how all the buttons are supposed to be placed
    [7, 8, 9, "/"],
    [4, 5, 6, "*"],
    [1, 2, 3, "-"],
    ["C", 0, "=", "+"]
]

# === BUTTON POSITIONING ===  # info on button placing
btn_height = 60
btn_width = 60
spacing_x = 10
spacing_y = 10
offset_x = 20
offset_y = 100

# === CREATE BUTTONS ===            # naming buttons and placing
buttons = {}                    # checks which are there                    
for row_index, row in enumerate(button_values): # sorts the button values into rows
    for col_index, val in enumerate(row): # sorts the rows into nums
        x = offset_x + col_index * (btn_width + spacing_x)
        y = offset_y + row_index * (btn_height + spacing_y)
        buttons[val] = createbutton(root, val, x, y)            #val is the name of said button
        print(buttons[val])                         
# === MAIN LOOP ===
root.mainloop()
