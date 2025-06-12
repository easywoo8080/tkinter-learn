import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.geometry('300x200')
root.title('Entry Widget Demo')

# 입력창
name_entry = ttk.Entry(root)
name_entry.pack()

name_entry = ttk.Entry(root)
name_entry.pack(pady=5)
# 포커스
name_entry.focus()

# 레이블과 함께 사용
email_label = ttk.Label(root, text='Email:')
email_label.pack(pady=2)

email_entry = ttk.Entry(root)
email_entry.pack(pady=5)


# 양방향 객체 연결
name_var = tk.StringVar()
name_entry = ttk.Entry(root, textvariable=name_var)
name_entry.pack()
name_entry.focus()


output_label = ttk.Label(root)
output_label.pack()

name_var.trace_add(
    "write", 
    lambda *args: output_label.config(text=name_var.get().upper())
)


# 2개의 엔트리 연결
# 하나의 StringVar를 생성
name_var = tk.StringVar()

# 두 개의 Entry에 동일한 StringVar를 연결
entry1 = ttk.Entry(root, textvariable=name_var)
entry1.pack()

entry2 = ttk.Entry(root, textvariable=name_var)
entry2.pack()

# 출력 라벨
output_label = ttk.Label(root)
output_label.pack()

# 입력값이 변경되면 라벨에 대문자로 표시
name_var.trace_add("write", lambda *args: output_label.config(text=name_var.get().upper()))

root.mainloop()