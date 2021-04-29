import tkinter as tk
from tkinter import ttk


Ui = tk.Tk()
Ui.title("Testing")
Ui.resizable(0,0)
label1 = ttk.Label(Ui,text="Testing")
label1.grid(column=0,row=0)
def clicked():
    button.configure(text = "I have been clicked")/6
    label1.configure(foreground = "red")
button = ttk.Button(Ui, text = "Click me", command = clicked)
button.grid(column = 1, row = 0)




Ui.mainloop()