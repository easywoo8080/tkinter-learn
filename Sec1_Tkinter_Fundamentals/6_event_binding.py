import tkinter as tk
from tkinter import ttk


def return_pressed(event):
    print('Return key pressed.')

## 뭐가 된다는 걸까요??..?
root = tk.Tk()
root.geometry('200x150')
entry = ttk.Entry(root)
entry.pack(pady=20)
entry.focus_set()


btn = ttk.Button(root, text='Save')
btn.bind('<Return>', return_pressed)


btn.focus()
btn.pack(expand=True)

root.mainloop()