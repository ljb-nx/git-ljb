#coding:utf-8
'''
Created on 2020-03-10
@author: ljb
'''
from urllib.request import urlopen, Request 
import re 
from bs4 import BeautifulSoup
from distutils.filelist import findall
 
 
 
# page = urllib.request.urlopen('http://movie.douban.com/top250?format=text')
# contents = page.read()
# contents = contents.decode('utf-8')




url = 'http://movie.douban.com/top250?format=text'
header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'}
ret = Request(url, headers=header)
res = urlopen(ret)
contents = res.read().decode('utf-8')


print(contents)
soup = BeautifulSoup(contents,"html.parser")
print("豆瓣电影TOP250" + "\n" +" 影片名              评分       评价人数     链接 ")  
for tag in soup.find_all('div', class_='info'):  
   # print tag
    m_name = tag.find('span', class_='title').get_text()      
    m_rating_score = float(tag.find('span',class_='rating_num').get_text())        
    m_people = tag.find('div',class_="star")
    m_span = m_people.findAll('span')
    m_peoplecount = m_span[3].contents[0]
    m_url=tag.find('a').get('href')
    print( m_name+"        "  +  str(m_rating_score)   + "           " + m_peoplecount + "    " + m_url )   




