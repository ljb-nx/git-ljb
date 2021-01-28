# coding:utf-8

import requests

resp = requests.get('https://www.douban.com/')  #豆瓣首页
print(resp.status_code)	# 418  这里状态码返回为418，很明显是请求不成功该网址的，下面再说如何处理
