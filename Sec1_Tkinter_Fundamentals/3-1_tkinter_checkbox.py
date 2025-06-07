import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo

root = tk.Tk()
root.geometry('200x150')
root.title('Checkbox Demo')


def show_message():
    showinfo(
        title='Result',
        message='You agreed.' if agreement_var.get() else 'You did not agree.'
    )


agreement_var = tk.BooleanVar()

checkbox = ttk.Checkbutton(
    root,
    text='I agree',
    command=show_message,
    variable=agreement_var
)

checkbox.pack()


root.mainloop()