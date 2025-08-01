import customtkinter as ctk
import tkinter as tk
root = tk.Tk()
  # Themes: "blue" (standard), "green", "dark-blue"
root.geometry("500x500")
root.title("This is a text for tkinter")
label = tk.Label(root, text="Hi im a label", font=('arial',18))

root.grid_columnconfigure(0, minsize=100)
root.rowconfigure(0, minsize=50)
def button(text):
    print (text, "has been pressed")

def createbutton(parent, text, x , y):
    return ctk.CTkButton(
        parent,
        text= str(text),
        font=('Arial', 24),
        command= lambda: button(text),
        bg_color="PeachPuff3",
        fg_color="PeachPuff1",
        text_color="Snow4",
        #background_corner_colors=(),
        corner_radius=15,
        hover_color = "PeachPuff2",
        height= 60,
        width= 60,
    ).place(x = y, y = y, pady = 5, padx= 5 )
        

for i in range(1, 10):
    createbutton(root, i, (i-1)//3, (i-1)%3)
createbutton(root, 0, 3, 1)

btnheight = 60
btnwidth = 60
spacing_x = 10  
spacing_y = 10  
offset_x = 20   
offset_y = 20   

for row_index, row in enumerate(button_values):
    for col_for row_index, row in enumerate(button_values):
    for col_index, val in enumerate(row):
        x = offset_x + col_index * (btn_width + spacing_x)
        y = offset_y + row_index * (btn_height + spacing_y)
        buttons[val] = create_button(root, val, x, y)index, val in enumerate(row):
        x = offset_x + col_index * (btn_width + spacing_x)
        y = offset_y + row_index * (btn_height + spacing_y)
        buttons[val] = create_button(root, val, x, y)


def buttonenter():
    print("Enter is pressed")




buttonenter = ctk.CTkButton( 
                    root, 
                    text= "Click me",
                    font=('Arial', 12),
                    command= buttonenter,
                    bg_color="light sky blue",
                    background_corner_colors=("white","white","white","white"),
                    corner_radius=15,
                    hover_color = "light blue",
                    height= 120,
                    width= 60
                    )

buttonenter.place(x=360,y=300 )












root.mainloop()