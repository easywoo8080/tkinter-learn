# Ttk 위젯

# 위젯 테마
# 전혀 버튼이 안생기는데...?
import tkinter as tk
from tkinter import ttk

root = tk.Tk()


# 창 크기 지정
width = 200
height = 150

# 화면 크기 가져오기
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# 창 왼쪽 상단 위치 계산 (화면 중앙)
x = (screen_width - width) // 2
y = (screen_height - height) // 2

# geometry 설정
root.geometry(f"{width}x{height}+{x}+{y}")

# Label은 라벨을 생성한다 ***사이트에선 Label이 Button을 생성한다고 되어있다.***
# tk.Label(root, text='Classic Label').pack()
# ttk.Label(root, text='Themed Label').pack()

# Button은 버튼을 생성한다
tk.Button(root, text='Classic Button').pack()
ttk.Button(root, text='Themed Button').pack()



root.mainloop()