#숫자를 입력 받고 입력받는 숫자만큼 랜덤 배열 생성
# v = np.array([
#     [1, 3, -9, 2],
#     [71, 13, -22, 7]
# ])
#
# print(v.ndim, v.shape, v.data, v.dtype, v.strides)
#
# number = list(map(int, input().split()))
# print(number)
#
# n = int(input("input number : "))
# l = list()
# for i in range(n):
#     l.append(random.randint(1, 100))
import numpy as np
import random
import tkinter as tk  # Built in GUI
from tkinter import messagebox #팝업 윈도우

def create_2d_array(row, col):
    matrix = np.random.randint(1, 101, size =(row, col))

def click_button():
    try:
        r, c = map(int, en_row_column.get().split())

        rows = [[random.randint(1, 100) for i in range(r)]for i in range(c)]
        matrix = np.array(rows, dtype='int16')
        lbl_result.config(text=matrix) #출력 결과를 나타내는 레이블을 만듬
    except ValueError as err:
        messagebox.showerror('Error!',f'입력 값이 없습니다. \n{err}')
        # messagebox.showwarning('Error!', f'입력 값이 없습니다. \n{err}')

window = tk.Tk()
window.title('numpy gui version v0.9')
window.geometry('300x150')

# create widget, 작성한 순서에 따라 ui가 구성
lbl_result = tk.Label(text="random numpy 2D array")
en_row_column = tk.Entry() #입력 상자
btn_click = tk.Button(text="click me!", command=click_button)

# widget layout
lbl_result.pack()
en_row_column.pack(fill='x')
btn_click.pack(fill='x')
# lbl_result.grid(row=0, column=0, columnspan=2)
# en_row.grid(row=1, column=0)
# en_col.grid(row=1, column=1)
# btn_click.grid(row=2, column=0, columnspan=2, sticky=tk.EW)
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
# print(v)




