#encoding=utf8
# 环境python3.7 
import requests
from bs4 import BeautifulSoup
import urllib.request
from  tkinter import *
import tkinter.messagebox as mbox

lists=[]
def download_music():
    headers = {
        'Referer':'http://music.163.com/',
        'Host':'music.163.com',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.75 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        }
    ids = entry.get()
    # 歌单的url地址
    play_url = 'http://music.163.com/playlist?id=' + str(ids)
     
    # 获取页面内容
    s = requests.session()
    response=s.get(play_url,headers = headers).content
     
    #使用bs4匹配出对应的歌曲名称和地址
    s = BeautifulSoup(response,'lxml')
    main = s.find('ul',{'class':'f-hide'})
     
     
    #lists=[]
    for music in main.find_all('a'):
        list=[]
        # print('{} : {}'.format(music.text, music['href']))
        musicUrl='http://music.163.com/song/media/outer/url'+music['href'][5:]+'.mp3'
        musicName=music.text
        # 单首歌曲的名字和地址放在list列表中
        list.append(musicName)
        list.append(musicUrl)
        # 全部歌曲信息放在lists列表中
        lists.append(list)
     
    #print(lists)
    
    # 下载列表中的全部歌曲，并以歌曲名命名下载后的文件，文件位置为当前文件夹
    for i in lists:
        url=i[1]
        name=i[0]
        try:
            lb.insert('end', name + '---->>>>正在下载')
            #print('正在下载',name)
            urllib.request.urlretrieve(url,'./%s.mp3'% name)
            #print('下载成功')
            lb.insert('end','---->>>>下载成功')
            
        except:
            print('下载失败')
            #lb.insert('end', name + '---->>下载失败')        
    
    mbox.showinfo("","==下载成功==")


root = Tk()
#1、窗口标题
 
res = StringVar()

root.title('音乐歌单下载')
#2、窗口大小，显示位置
root.geometry('500x400')
#3、标签控件
lable = Label(root,text='输入网易音乐播放歌单的Id',font=('微软雅黑',10), fg='black')
lable.grid(row=0,column=0,padx=(5,0),pady=5,sticky=W)

#4、输入控件
entry=Entry(root, font='微软雅黑')
entry.grid(row=1,column=0,padx=(5,0),pady=5,sticky=W)

#5、按钮控件
button = Button(root, text ="下载",width=10,font=('微软雅黑',10),command=download_music)
button.grid(row=0,column=1,sticky=W)
 
button1 = Button(root, text ="退出",width=10,font=('微软雅黑',10), command=root.quit)
button1.grid(row=1,column=1,sticky=W)

yscroll = Scrollbar(root, orient=VERTICAL)
yscroll.grid(row=2,column=2,rowspan=4,padx=(0,5),pady=5,sticky=NS)

# 创建Listbox
lb = Listbox(root,width=40,yscrollcommand=yscroll.set)

lb.grid(row=2,column=0,columnspan=2,rowspan=4,padx=(5,0),pady=5,sticky=W)
yscroll["command"] = lb.yview

#-----------------至此，界面已经画出来了---------------------------
 
root.mainloop()