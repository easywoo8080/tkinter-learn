import tkinter as tk
from tkinter import ttk


root = tk.Tk()
root.geometry('600x400+50+50')
ttk.Label(root, text='Hi, there').pack()

label = ttk.Label(root)
label['text'] = 'Hi, there2'
label.pack()

# pack이 최근에 저장된 label을 찍나?
label.pack()
ttk.Label(root, text='Hi, there3').pack()

label = ttk.Label(root)
label['text'] = 'Hi, there4'
label.pack()
root.mainloop()