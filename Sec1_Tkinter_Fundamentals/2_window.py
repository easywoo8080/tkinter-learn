import tkinter as tk

root = tk.Tk()


# set the title of the window
# ko: 창의 제목 설정
root.title("My First Tkinter Window")

# set the size of the window
# ko: 창의 크기 설정
root.geometry('600x400+50+50')

# set the background color of the window
# ko: 창의 배경색 설정
root.attributes('-alpha', 0.5)
root.mainloop()

