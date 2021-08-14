import requests
from bs4 import BeautifulSoup


resLandingPageUrl='https://www.ptt.cc/ask/over18?from=%2Fbbs%2FGossiping%2Findex.html'
askOver18Url = 'https://www.ptt.cc/ask/over18'
pttGossipUrl='https://www.ptt.cc/bbs/Gossiping/index.html'

userAgent='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36'
headers= {
    'User-Agent' : userAgent
}
ss = requests.session()

resLandingPage = ss.get(resLandingPageUrl,headers=headers)
soupLandingPage = BeautifulSoup(resLandingPage.text,'html.parser')
print(ss.cookies)

# print(res.text)

data=dict()
key1=soupLandingPage.select('input')[0]['name']
value1=soupLandingPage.select('input')[0]['value']
data[key1] =value1

key1=soupLandingPage.select('button')[0]['name']
value1=soupLandingPage.select('button')[0]['value']
data[key1] =value1

print(data)
ss.post(askOver18Url,headers=headers,data=data)
print(ss.cookies)

res = ss.get(pttGossipUrl,headers=headers)
print(res.text)