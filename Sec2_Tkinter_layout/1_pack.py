import tkinter as tk

root = tk.Tk()
root.title('Tkinter Pack Layout')
root.geometry('600x400')

tk.Label(root, text='Tkinter',bg='red',fg='white').pack()
tk.Label(root,text='Pack Layout',bg='green', fg='white').pack()
tk.Label(root, text='Demo',bg='blue', fg='white').pack()

# red, green, blue 순서대로 위젯이 쌓인다.

# 의도적으로 상단정렬을 합니다.
tk.Label(root, text='Tkinter top',bg='red',fg='white').pack(side=tk.TOP)
tk.Label(root,text='Pack Layout top',bg='green', fg='white').pack(side=tk.TOP)
tk.Label(root, text='Demo top',bg='blue', fg='white').pack(side=tk.TOP)


#  하단정렬을 합니다.
tk.Label(root, text='Tkinter bottom',bg='red',fg='white').pack(side=tk.BOTTOM)
tk.Label(root,text='Pack Layout bottom',bg='green', fg='white').pack(side=tk.BOTTOM)
tk.Label(root, text='Demo bottom',bg='blue', fg='white').pack(side=tk.BOTTOM)



#  왼쪽 정렬을 합니다.
tk.Label(root, text='Tkinter LEFT',bg='red',fg='white').pack(side=tk.LEFT)
tk.Label(root,text='Pack Layout LEFT',bg='green', fg='white').pack(side=tk.LEFT)
tk.Label(root, text='Demo LEFT',bg='blue', fg='white').pack(side=tk.LEFT)


#  우측 정렬을 합니다.
tk.Label(root, text='Tkinter RIGHT',bg='red',fg='white').pack(side=tk.RIGHT)
tk.Label(root,text='Pack Layout RIGHT',bg='green', fg='white').pack(side=tk.RIGHT)
tk.Label(root, text='Demo RIGHT',bg='blue', fg='white').pack(side=tk.RIGHT)

root.mainloop()

