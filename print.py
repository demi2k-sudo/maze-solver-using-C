import tkinter as tk
from tkinter import messagebox

win = tk.Tk()
win.title("Welcome")
win.geometry('700x350')
def click():
    messagebox.showinfo("Hey",'You have clicked')
    
b = tk.Button(win, text = 'Submit', command=click, activebackground='orange', activeforeground='red',pady=10,padx=5)
b.pack()

win.mainloop()