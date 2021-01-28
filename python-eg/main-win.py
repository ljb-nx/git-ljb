#!/usr/bin/python
# -*- coding: UTF-8 -*-  
import wx
import myframe1
import sys 
# reload(sys) 
# sys.setdefaultencoding('utf-8')
 
 
class MianWindow(myframe1.MyFrame1):
    # 首先，咱们从刚刚源文件中将主窗体继承下来.就是修改过name属性的主窗体咯。
   def init_main_window(self):
       self.m_staticText1.label = ""  
   def main_button_click(self, event):
       self.m_staticText1.label = "hello world!"
       
if __name__ == '__main__':
    app = wx.App()
  
    main_win = MianWindow(None)
    main_win.init_main_window()
    main_win.Show()
    app.MainLoop()
