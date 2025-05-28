
import tkinter as tk
from tkinter import ttk

# 요약:
# - 단순 출력은 한 줄로 처리
# - 속성 수정이 필요하면 변수에 저장


root = tk.Tk()
root.geometry('600x400+50+50')

# 1. 한 줄 생성 및 배치
ttk.Label(root, text='Hi, there').pack()
# - 위젯을 생성하고 바로 배치
# - 변수에 저장하지 않아 이후 수정 불가

# 2. 변수에 저장한 후 배치
label = ttk.Label(root)
label['text'] = 'Hi2'
label.pack()
# - 위젯을 나중에 수정하거나 재사용 가능


# pack이 최근에 저장된 label을 찍나?
# 3. 같은 위젯에서 .pack() 여러 번 호출
label.pack()
label.pack()
label.pack()

# 결과는 No!
# - 같은 위젯을 반복 배치해도 중복 표시되지 않음
# - 이미 배치된 상태이면 무시되거나 위치 재조정만 됨


ttk.Label(root, text='Hi, there3').pack()

label = ttk.Label(root)
label['text'] = 'Hi, there4'
label.pack()


root.mainloop()