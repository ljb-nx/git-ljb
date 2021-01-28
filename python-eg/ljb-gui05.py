#!/usr/bin/python
# coding:utf-8

import tkinter as tk
 
 
# 设置窗口
window = tk.Tk()  # 建立一个窗口
window.title('一个最简单的窗口')
window.geometry('300x200')  # 窗口大小为300x200
 
 
bon = False
 
 
def hit_me():  # 该函数实现按一次按钮显示出字，再按一次字消失
    global bon  # bon为全局变量
    if bon == False:
        bon = True
        var.set('惊喜想得美')
    else:
        bon = False
        var.set('')
 
  
var = tk.StringVar()  # 文字变量储存器
 
 
# 设置标签
l = tk.Label(textvar=var, bg='yellow', width=20, height=2)  # 参数textvar不同于text,bg是backgroud
l.pack()  # 放置标签
 

# 设置按钮
b = tk.Button(text='点击我有惊喜', width=20, height=2, command=hit_me)
b.pack()
 
 
window.mainloop()  # 循环，时刻刷新窗口
