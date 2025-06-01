````markdown
# Tkinter 기초 정리

---

## 1. 창 만들기 (Tkinter Hello, World!)

- `tkinter` 모듈 import 후, `root = tk.Tk()`로 기본 창 생성
- `root.mainloop()`를 호출해야 창이 화면에 유지됨 (필수)
- 보통 `mainloop()`를 마지막에 배치함
- 기본 창 변수명은 관례적으로 `root` 사용 (다른 이름 가능)

```python
import tkinter as tk

root = tk.Tk()

# 1000ms(1초) 후에 창 닫기 함수 실행 (예: 3000ms = 3초)
root.after(3000, root.destroy)

root.mainloop()
````

> **오류 안내**
> ImportError: No module named Tkinter 발생 시,
> 우분투 환경에서는 `sudo apt-get install python3-tk` 설치 필요

---

## 2. 윈도우 속성 조절 (크기, 위치, 투명도, 제목)

* 창 제목: `root.title("타이틀 이름")`
* 창 크기 및 위치: `root.geometry('가로x세로+x좌표+y좌표')`

  * 가로, 세로: 실제 창 크기(px)
  * x, y: 모니터 좌상단 기준 창 위치 이동(px)
* 투명도: `root.attributes('-alpha', 투명도)` (0.0 \~ 1.0)

```python
import tkinter as tk

root = tk.Tk()

root.title("My First Tkinter Window")
root.geometry('600x400+500+500')
root.attributes('-alpha', 0.5)

root.mainloop()
```

---

## 3. 테마 위젯 (Themed Widget)

* 기본 Tkinter 위젯: `tk.Button`
* 테마가 적용된 위젯: `ttk.Button` (ttk 모듈 사용)
* 내장 테마 종류 (OS별 다름):
  `default`, `classic`, `alt`, `clam`(주로 사용), `vista`(Windows), `xpnative`(Windows), `aqua`(macOS)

```python
import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.geometry('600x400+50+50')

tk.Button(root, text='Classic Button').pack()
ttk.Button(root, text='Themed Button').pack()

root.mainloop()
```

* 더 많은 테마: [ttkthemes 공식문서](https://ttkthemes.readthedocs.io/en/latest/)
* 설치: `pip install ttkthemes`

```python
from tkinter import Tk
from ttkthemes import ThemedTk

root = ThemedTk(theme="arc")  # 예: 'arc', 'breeze', 'plastik' 등
root.mainloop()
```

---

## 4. 버튼 클릭 이벤트 (Command Button)

* 버튼 클릭 시 호출할 콜백 함수는 `command` 속성에 함수명만 전달 (괄호 없이)
* 콜백에 인자 전달 시, `lambda` 또는 `functools.partial` 사용

```python
import tkinter as tk
from tkinter import ttk
from functools import partial

root = tk.Tk()

def button_clicked():
    print('Button clicked')

ttk.Button(root, text='Click Me', command=button_clicked).pack()

def callback_function(args):
    print('Callback called with args:', args)

ttk.Button(root, text='Rock', command=lambda: callback_function('Rock')).pack()

ttk.Button(root, text='lambda_1', command=lambda: print('lambda_1')).pack()
ttk.Button(root, text='lambda_2', command=partial(print, 'lambda_2')).pack()

def on_button_click(text):
    print('Button clicked with arg:', text)

ttk.Button(root, text='lambda_3', command=partial(on_button_click, 'lambda_3')).pack()

root.mainloop()
```

### `lambda` vs `partial` 차이

| 구분     | lambda                  | partial               |
| ------ | ----------------------- | --------------------- |
| 정의 방식  | 익명 함수, 직접 인자 전달         | 기존 함수에 인자 미리 바인딩      |
| 문법     | `lambda: func(args)`    | `partial(func, args)` |
| 가독성    | 간단한 경우 직관적, 복잡하면 가독성 저하 | 명확한 함수 바인딩 표현         |
| 재사용성   | 익명 함수라 재사용 불가           | 함수 객체 재사용 가능          |
| 기능 확장성 | 여러 동작 작성 가능             | 함수 + 인자 고정 용도         |

* **요약**

  * 간단한 콜백: `lambda`가 직관적
  * 인자 고정 콜백 여러 개 반복 사용: `partial`이 깔끔하고 재사용 가능

---

# 결론

* Tkinter 기본 창 생성과 유지에는 `Tk()` + `mainloop()` 필수
* 창 크기, 위치, 투명도, 제목 설정은 `geometry()`, `attributes()`, `title()` 활용
* 테마 위젯은 `ttk` 사용, 필요 시 `ttkthemes` 설치하여 확장 가능
* 버튼 이벤트 콜백은 `command` 속성에 함수 전달, 인자 필요시 `lambda` 또는 `partial` 사용

---