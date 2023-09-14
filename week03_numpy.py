import numpy as np
import random
import tkinter as tk  # Built in GUI
from tkinter import (messagebox)  # 팝업 윈도우

def press_enter_key(ev):
    click_button()
    messagebox.showinfo('x, y', f"({ev.x},{ev.y})")

def click_button():
    try:
        r, c = map(int, en_row.get().split())
        matrix = np.random.randint(1, 101, size=(r, c))
        lbl_result.config(text=matrix)  # 출력 결과를 나타내는 레이블을 만듬
    except ValueError as err:
        messagebox.showerror('Error!', f'입력 값이 없습니다. \n{err}')

window = tk.Tk()
window.title('numpy gui version v0.9')
window.geometry('300x150')

# create widget, 작성한 순서에 따라 ui가 구성
lbl_result = tk.Label(text="random numpy 2D array")
en_row = tk.Entry()  # 입력 상자
btn_click = tk.Button(text="click me!", command=click_button)

en_row.bind("<Return>", press_enter_key)
# widget layout
lbl_result.pack()
en_row.pack(fill='x')
btn_click.pack(fill='x')

en_row.focus()
# 격자배열
# lbl_result.pack()
# en_row.pack(fill='x')
# en_col.pack(f)
# btn_click.pack(fill='x')
# 행렬배열
# lbl_result.grid(row=0, column=0, columnspan=2)
# en_number.grid(row=1, column=0)
# btn_click.grid(row=1, column=1)
# 절대좌표값
# lbl_result.place(x=50, y=50)
window.mainloop()
# n = int(input("input number : "))
# l = [random.randint(1, 100) for i in range(n)]
# v = np.array(l, dtype='int16')