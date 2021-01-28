import requests
import json
from lxml import etree
#import jsonpath
def saveSound(url,song_name):

	# print(response.content)
	root='E://ljb-python/%s.mp3'%song_name
	with open(root,'wb') as f:
		header={
		"Origin": "https://music.163.com",
		"Referer": "https://music.163.com/",
		"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.109 Safari/537.36"
	}
		r=requests.get(url,headers=header)
		f.write(r.content)
		# with open('')
def getHTML(url):
	header={
	"Origin": "https://music.163.com",
    "Referer": "https://music.163.com/",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.109 Safari/537.36"
	}
	response=requests.get(url,headers=header)
	response.encoding='utf-8'
	html=response.text
	tree=etree.HTML(html)
	url=tree.xpath('//ul[@class="f-hide"]/li/a/@href')
	song_name=tree.xpath('//ul[@class="f-hide"]/li/a/text()')
	for index,i in enumerate(url):
		every_url=i.split('=')[-1]
		song=song_name[index]
		base_url='http://music.163.com/song/media/outer/url?id=%s'%every_url
		print('第'+str(index+1)+'数据保存成功')
		saveSound(base_url,song)
getHTML('https://music.163.com/playlist?id=924680166')

