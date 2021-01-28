# coding:utf-8

import requests
from bs4 import BeautifulSoup
import lxml

url = 'https://cn.tripadvisor.com/Attractions-g60763-Activities-New_York_City_New_York.html'
header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'}

wb_data = requests.get(url,headers=header)
soup = BeautifulSoup(wb_data.text,'lxml')
#print(soup)

#titles = soup.select('#taplc_attraction_coverpage_attraction_0 > div > div:nth-child(1) > div > div > div.shelf_item_container.shelfItemsWithGrayBgWrapper > div:nth-child(3) > div.poi > div > div.item.name > a')
#titles = soup.select('div.item.name > a')
#print(titles)

cates = soup.select('div.p13n_reasoning_v2')
for cate in cates:
    cate_list = list(cate.stripped_strings)
    for one_cate in cate_list:
        if one_cate == ',':
            cate_list.remove(one_cate)
    print(cate_list)
