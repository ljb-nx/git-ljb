# coding:utf-8
import requests
import time
import random
import pandas as pd
import re
#构造请求头
headers = {
'Accept':'*/*',
'Accept -Enconding':'gzip,deflate',
'Accept-Language':'zh-CN,zh;q=0.9',
'conection':'keep-alive',
'User-Agent':'Mozilla/5.0  (windows NT 6.1;  WOW64)  AppleWebKit/537.36 (KHTML,like Gecko) Chrome/63.0.3236.0 Safari/537.36'
}
#生成所有需要抓取的链接
urls = []
for year in range(2012,2019):
    for month in range(1,13):
        if year <= 2016:
　　　　    urls.append('http://tianqi.2345.com/t/wea_history/js/58362_%s%s.js'
                    %(year,month))
        else:
　　　　    if month<10:
                urls.append('http://tianqi.2345.com/t/wea_history/js/58362_%s%s.js' %(year,month,year,month))
#循环并通过正则匹配获取相关数据
info = []
for url in urls:
　　seconds random.randint(3,6)
　　response = requests.get(usl,headers = headers).text    #发送url链接的请求,并返回响应数据
ymd =re.findall("ymd:'(.*?)',",response)   #正则表达式获取日期数据
high = re.findall("bWendu:'(.*?)',",response)  #正则表达式获取最高气温数据
low = re.findall("yWendu:'(.*?)',",response)   #正则表达式获取最低气温数据
tianqi = re.findall("tianqi:'(.*?)',",response)   #正则表达式获取天气状况数据
fengxiang = re.findall("fengxiang:'(.*?)',",response)  # 正则表达式获取风向数据
fengli = re.findall("fengli:'(.*?)',",response)   #正则表达式获取风力数据
aqi = re.findall("aqi:'(.*?)',",response)  #正则表达式获取空气质量指标数据
aqiInfo = re.findall("aqiInfo:'(.*?)',",response)  #正则表达式获取空气质量说明数据
aqiLevel = re.findall("aqiLevel:'(.*?)',",response)  #正则表达式获取空气质量水平数据
#犹豫 2012-2015没有空气质量相关的数据，故需要分开处理
if len(aqi) == 0:
　　aqi = None
　　aqiInfo = None
　　aqiLevel = None
　　info.append(pd.DataFrame({'ymd':ymd,'high':high,'low':low,'tianqi':tianqi,
　　　　　　　　　　　　　　'fengxiang':fengxiang,'fengli':fengli,'aqi':aqi,
　　　　　　　　　　　　　　'aqiInfo':aqiInfo,'aqiLevel':aqiLevel}))
else:
　　info.append(pd.DataFrame({'ymd':ymd,'high':high,'low':low,'tianqi':tianqi,
　　　　　　　　　　　　　　'fengxiang':fengxiang,'fengli':fengli,'aqi':aqi,
　　　　　　　　　　　　　　'aqiInfo':aqiInfo,'aqiLevel':aqiLevel}))
　　time.sleep(seconds)     #每循环一次，都随机停顿几秒
#将存储的所有天气数据进行合并，生成数据表格
weather = pd.concat(info)
#数据导出
weather.to_csv('weather.csv',index = False)
