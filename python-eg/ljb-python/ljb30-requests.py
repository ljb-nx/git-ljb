import re
import urllib.request
import pandas as pd
import csv
import os
 
#创建文件夹
def build_folder():
    file='C:\\Users\\Administrator\\Desktop\\中商情报网各类商品信息'
    os.makedirs(file)
build_folder()
#从主页爬取商品名称
html=urllib.request.urlopen("http://s.askci.com/data/quarterindustry/").read()
html=html.decode('utf-8')
regex='<a class="" href="(.*)">(.*)</a>'
regex=re.compile(regex)
industry=re.findall(regex,html)
#创建资源名称列表
resorce_name_list=[]
resorce_id_list=[]
#将名称和ID填入列表
for name in industry:
    resorce_name_list.append(name[1])
    a=name[0]
    resorce_id_list.append(a[-7:])
#爬取各条商品的表格
count=0
for resorce_id in resorce_id_list:
    form=pd.read_html("http://s.askci.com/data/quarterindustry/{}/".format(str(resorce_id)))[0]
    resorce_name=resorce_name_list[count]
    #将内容写入CSV文件
    #注意，文件夹名字不能有<>/\:*?|"
    #应当事先检查要创建的文件夹名称
    try:
        form.to_csv(r'C:\\Users\\Administrator\\Desktop\\中商情报网各类商品信息\\{}.csv'.format(resorce_name), mode='a', encoding='utf_8_sig', header=1, index=0)
    except FileNotFoundError:
        newname=resorce_name.replace('/','')
        form.to_csv(r'C:\\Users\\Administrator\\Desktop\\中商情报网各类商品信息\\{}.csv'.format(newname), mode='a', encoding='utf_8_sig', header=1, index=0)
    count+=1
    print('正在爬取{}。。。'.format(resorce_name))
print('程序已完成')
