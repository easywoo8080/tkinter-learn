from functools import partial
import tkinter as tk
from tkinter import ttk

# main window
root = tk.Tk()
root.geometry('300x200')
root.resizable(False, False)
root.title('Button Demo')


def callback():
    print('Button clicked!')
    # do something

# 위의 callback 함수를 덮어써서 아래의 callback 함수를 사용합니다.
def callback(name):
    print(f'Hello, {name}')
    # do something

# callback argument가 없다고 error발생
ttk.Button(
   root, 
   text="Click Me", 
   command=callback
).pack(
    ipadx=5,
    ipady=5,
    expand=True
)


# callback argumnet에 Alice를 전달
ttk.Button(
   root, 
   text="Click Me", 
   command=partial(callback, 'Alice')
).pack(
    ipadx=2,
    ipady=2,
    expand=False
)


# exit button
exit_button = ttk.Button(
    root,
    text='Exit',
    command=lambda: root.quit()
)

exit_button.pack(
    ipadx=5,
    ipady=5,
    expand=True
)

root.mainloop()