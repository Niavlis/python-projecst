import tkinter as tk
from tkinter import font
root = tk.Tk()
root.title("Grid Visualization")

for row_idx in range(3):
            for col_idx in range(3):
                frame = tk.Frame(
                    master=root,
                    relief=tk.RAISED,
                    borderwidth=1,
                    bg=f"{row_idx * 50}{col_idx * 50}red"  # Example: varying color
                )
                frame.grid(row=row_idx, column=col_idx, padx=5, pady=5)
                label = tk.Label(master=frame, text=f"R{row_idx}C{col_idx}")
                label.pack(padx=10, pady=10)

root.mainloop()