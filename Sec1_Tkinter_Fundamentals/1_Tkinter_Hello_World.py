import tkinter as tk

root = tk.Tk()

# 1000ms (1초) 후에 창 닫기 함수 실행
root.after(3000, root.destroy)

root.mainloop()

