#!/usr/bin/python
# coding:utf-8

import tkinter as tk
 
 
# 设置窗口
window = tk.Tk()
window.title('插入字符的窗口')
# window.geometry('500x300')
window.geometry('500x300+200+200') 
 
# 该函数的功能是在光标处插入字符串
def insert_point():
    var1 = e.get()
    t.insert('insert', var1)  # 参数insert表示在光标处插入字符串
 
 
# 该函数的功能是在光标处插入字符串
def insert_end():
    var2 = e.get()
    t.insert('end', var2)  # 参数end表示在光标处插入字符串 


# 设置输入窗口
e = tk.Entry()
e.pack()
 
 
# 设置两个插入按钮
b1 = tk.Button(text='在光标处插入', width=20, height=2, command=insert_point)
b1.pack()
b2 = tk.Button(text='在末尾处插入', width=20, height=2, command=insert_end)
b2.pack()
 
 
# 设置文本显示框
t = tk.Text(width=20, height=2)
t.pack()


window.mainloop()
