import tkinter as tk
from tkinter import ttk

# Main window
root = tk.Tk()
root.geometry('300x200')
root.title('Label Widget Demo')

# 텍스트 크기 및 폰트 변경
label = ttk.Label(root, text='This is a label')
label.pack()

label = ttk.Label(
    root,
    text='A Label with the Helvetica font',
    font=("Helvetica", 14))
label.pack()

# 이미지 출력 방법
photo = tk.PhotoImage(file='./assets/python.png')
image_label = ttk.Label(
    root,
    image=photo,
    padding=5
)
image_label.pack()

root.mainloop()

