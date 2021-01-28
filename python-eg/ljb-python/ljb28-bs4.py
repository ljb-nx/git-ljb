import urllib.request
import re
import bs4

#获取首页html内容
url_home = 'http://www.5bug.wang'
response = urllib.request.urlopen(url_home)
html = response.read().decode('utf8')

#使用正则表达式来匹配所有的文章链接
soup = bs4.BeautifulSoup(html, 'html.parser')
pattern = 'http://www.5bug.wang/([\s\S]*)\.html'
links = soup.find_all('a', href=re.compile(pattern))
url_set = set()
for link in links:
    url_set.add(link['href'])

#根据抓取到的文章链接，来进一步抓取文章页面具体信息
for url in url_set:
    response = urllib.request.urlopen(url)
    html = response.read().decode('utf8')
    soup = bs4.BeautifulSoup(html, 'html.parser')
    page = soup.find('div',{'class', 'content'})
    url = url
    title = page.find('h1').get_text()
    author = page.find('h4').get_text()
    content = page.find('article').get_text()
    #print(title, url, author, content)
    print(title, url, author)  #为了截图，不打印具体的文章内容信息

print('抓取完成!=====================================================')
