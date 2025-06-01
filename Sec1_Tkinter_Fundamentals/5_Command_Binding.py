# 요약 : 이 튜토리얼에서는 위젯 이벤트와 콜백을 연결하는 Tkinter 명령 바인딩에 대해 알아봅니다.


import tkinter as tk
from tkinter import ttk

root = tk.Tk()


# 먼저 콜백함수 정의!
def button_clicked():
    print('Button clicked')

# 람다 함수를 사용하여 콜백 함수에 인자를 전달하는 방법을 보여줍니다.
def callback_function(args):print('Callback function called with args:', args)

button = ttk.Button(root, text='Click Me', command=button_clicked)
button.pack()


ttk.Button(root, text='Rock', command=lambda: callback_function('Rock')).pack()
ttk.Button(root, text='Paper',command=lambda: callback_function('Paper')).pack()
ttk.Button(root, text='Scissors', command=lambda: callback_function('Scissors')).pack()


# 정인영님의 람다식을 이용해보자

from functools import partial

ttk.Button(root, text='lambda_1', command=lambda: print('lambda_1')).pack()


# partial을 사용하여 콜백 함수에 인자를 전달하는 방법을 보여줍니다.
ttk.Button(root, text='lambda_2', command=partial(print, 'lambda_2')).pack()


def on_button_click(text):
    print('Button clicked with no args : ', text)

# partial는 기존의 함수를 호출하여 사용할 수 있다.
ttk.Button(root, text='lambda_3', command=partial(on_button_click, 'lambda_3')).pack()

# ttk.Button(root, text='lambda_4', cogmmand=on_button_click('lambda_4')).pack()
           
root.mainloop()