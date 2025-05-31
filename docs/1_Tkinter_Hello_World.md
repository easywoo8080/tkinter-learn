
# s1
## 창만들기 (Tkinter Hello, World!)
[1_Tkinter Hello, World!](../Sec1_Tkinter_Fundamentals/1_Tkinter_Hello_World.py)


`tkinter`를 import한 뒤 `root`변수에 `Tk()`로 할당하여 사용함.

`mainloop()`를 사용하여야 메인 창이 화면에 표시됨. 그렇지 않으면 창은 즉시 사라지며, 사용자는 인식 불가능함

보통 마지막 명령문으로 `mainloop`를 배치합니다.

> 관례적으로 기본창의 변수명은 `root`로 합니다. 
> `window`도 사용하기도 하며 다른 이름을 지정하여 사용할 수 있다.


> [!error] ImportError: No module named Tkinter
> 우분투에서 위와 같은 에러가 발생할 수 있습니다. 아래를 설치하세요
> `sudo apt-get install python3-tk`

```py
import tkinter as tk

root = tk.Tk()

# 1000ms (1초) 후에 창 닫기 함수 실행
root.after(3000, root.destroy)

root.mainloop()
```


## Window

- 윈도우의 창 크기, 투명도를 조절합니다.
- title name
    - title("타이틀 이름")
- 크기 조절
    - geometru('width x height + x + y) 형태로 창 크기 설정
    - width와 heigth는 실제 창의 크기
    - x와 y는 주 모니터의 좌측 상단 (0,0) 에서 오른쪽으로 x만큼, 아래로 y만큼 이동한 위치에 창의 왼쪽 위가 위치
    - geometry('600x400+50+50')
- 투명도
    - attributes('-alpha', 0.5)


```py
import tkinter as tk

root = tk.Tk()


# set the title of the window
# ko: 창의 제목 설정
root.title("My First Tkinter Window")

# set the size of the window
# ko: 창의 크기 설정
root.geometry('600x400+500+500')

# set the background color of the window
# ko: 창의 배경색 설정
root.attributes('-alpha', 0.5)
root.mainloop()

```