import requests
import traceback
from bs4 import BeautifulSoup
import os
import json


if not os.path.exists('F:\python_code\pyETLProject\104Practice\ ') :
    os.mkdir('F:\python_code\pyETLProject\104Practice\ ')

searchUrl = 'https://www.104.com.tw/jobs/search/'
areaJsonUrl = 'https://static.104.com.tw/category-tool/json/Area.json'

userAgent='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36'
headers= {
    'User-Agent' : userAgent
}

ss = requests.session()

#處理地區JSON
areaJson = ss.get(areaJsonUrl,headers=headers).content
areaJsonObj=json.loads(areaJson)

#areaName =input('請輸入查詢的地區')
#jobName = input('請輸入查詢的職位')
jobName ='數據分析師'
areaName = '台北市'

#比對areaJson與areaName
def getAreaNo(areaJsonObj,areaName):
    for i in areaJsonObj:
        if (i['des'] in areaName):
            return i['no']
        elif i.get('n'):
            result = getAreaNo(i['n'],areaName)
            if(result != None):
                return result
                break
        else:
            continue


queryAreaNo =getAreaNo(areaJsonObj,areaName)
print(areaName in '')
payload = {'ro': '0', 'keyword': jobName,'jobsource':'2018indexpoc','expansionType':'job'}
if(areaName not in ''):
    payload['area']=queryAreaNo


searchRes = ss.get(searchUrl, headers=headers,params=payload)
soupSearchResult =BeautifulSoup(searchRes.text, 'html.parser')
#searchResultJson=soupSearchResult.select('script[type="application/ld+json"]')
scriptTag=soupSearchResult.find('script',type="application/ld+json")

searchResultJsonObj=json.loads(scriptTag.string)

for i in searchResultJsonObj:
    if((i.get('url') != None) & (i.get('organizer') != None)):
        articleUrl=i['url']
        artcleID=articleUrl.split('/')[-1]
        artRes = ss.get(articleUrl, headers=headers)

        contentUrl = 'https://www.104.com.tw/job/ajax/content/{}'
        headers["Referer"] = articleUrl
        contentRes = ss.get(contentUrl.format(artcleID), headers=headers)
        contentJson = json.loads(contentRes.text,)
        print(contentJson)
        break
