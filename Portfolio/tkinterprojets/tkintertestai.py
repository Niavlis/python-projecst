import tkinter as tk

root = tk.Tk()
root.title("Row and Column Sizing Example")

# Configure row 0: minimum size of 50 pixels, weight of 1 for stretching
root.rowconfigure(0, minsize=5, weight=1)
# Configure row 1: minimum size of 30 pixels, weight of 2 for more stretching
root.rowconfigure(1, minsize=1, weight=2)

# Configure column 0: minimum size of 80 pixels, weight of 1
root.columnconfigure(0, minsize=1, weight=1)
# Configure column 1: minimum size of 120 pixels, weight of 3 for more stretching
root.columnconfigure(1, minsize=1, weight=3)

root.geometry("500x500")

button = tk.Button(
                    text="Click me",
                    font=('Arial', 10)
                   
                   )
button.grid(row = 0, column= 0)


root.mainloop()