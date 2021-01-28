#/usr/bin/python
# coding:utf-8

import tkinter as tk
import tkinter.simpledialog as dl
import tkinter.messagebox as mb

root = tk.Tk()

w = tk.Label(root,text="Label Title")
w.pack()

mb.showinfo("welcome","welcome message.")
guess = dl.askinteger("number","Enter a number:")


mb.showinfo("",guess)
