import urllib.request
import urllib.parse
import json

#通过抓包的方式获取post的url，并不是浏览器地址栏的url
url = "http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule"
#用户接口输入
key=input("请输入需要翻译的文字:")
#发送到web服务器的表单数据
formdata ={
    "i": key,
    "from": "AUTO",
    "to": "AUTO",
    "smartresult": "dict",
    "client": "fanyideskweb",
    "salt": "1537698317221",
    "sign": "b569c8bf54bf1b0d71725726e7c1a5",
    "doctype": "json",
    "version": "2.1",
    "keyfrom": "fanyi.web",
    "action": "FY_BY_REALTIME",
    "typoResult": "false"
    }
#headers
headers={ "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36"}
#经过urlencode转码
data = urllib.parse.urlencode(formdata).encode(encoding='gbk')
#如果Request（）方法里的data参数里有值，那么这个请求就是post
#如果没有，则是get请求
request = urllib.request.Request(url,data=data, headers = headers)

repost = urllib.request.urlopen(request)

html=repost.read().decode("utf-8")
# print(html)

infos = json.loads(html)
if 'translateResult' in infos:
    try:
        result = infos['translateResult'][0][0]['tgt']
        print("翻译：")
        print(result)
    except:
        pass
