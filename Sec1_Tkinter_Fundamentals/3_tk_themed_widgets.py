# Ttk 위젯

# 위젯 테마
# 전혀 버튼이 안생기는데...?
import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.geometry('600x400+50+50')

# Label은 라벨을 생성한다 ***사이트에선 Label이 Button을 생성한다고 되어있다.***
tk.Label(root, text='Classic Label').pack()
ttk.Label(root, text='Themed Label').pack()

# Button은 버튼을 생성한다
tk.Button(root, text='Classic Button').pack()
ttk.Button(root, text='Themed Button').pack()



root.mainloop()