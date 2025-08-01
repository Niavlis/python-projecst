import customtkinter as ctk
import tkinter as tk
root = tk.Tk()
ctk.set_default_color_theme("green")  # Themes: "blue" (standard), "green", "dark-blue"
root.geometry("500x500")
root.title("This is a text for tkinter")
label = tk.Label(root, text="Hi im a label", font=('arial',18))

root.grid_columnconfigure(0, minsize=100)
root.rowconfigure(0, minsize=50)




def buttonclick():
    print("Button 1 is pressed")
def buttonclick2():
    print("Button 2 is pressed")




button = ctk.CTkButton( root, text= "Click me",
                    font=('Arial', 13),
                    command= buttonclick,
                    bg_color="sky blue",
                    background_corner_colors=("white","white","white","white"),
                    corner_radius=20,
                    hover_color = "light blue",
                    
                    )
button2 = tk.Button( root, text= "Click me", font=('Arial', 13), command= buttonclick2)

button.place(x=300,y=400 )












root.mainloop()