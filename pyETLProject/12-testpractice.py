import requests
from bs4 import BeautifulSoup

url='http://ec2-13-114-140-26.ap-northeast-1.compute.amazonaws.com/practice/tfb103'

userAgent='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36'
headers= {
    'User-Agent' : userAgent
}
ss = requests.session()

resLandingPage = ss.get(url,headers=headers)
soupLandingPage = BeautifulSoup(resLandingPage.text,'html.parser')
# print(ss.cookies)
# print(soupLandingPage)

data=dict()
key1=soupLandingPage.select('input[type="hidden"]')[0]['name']
value1=soupLandingPage.select('input[type="hidden"]')[0]['value']
data[key1] =value1


# key2=soupLandingPage.select('input[type="textbox"]')[0]['name']
# value2='Allen'
# data[key2] =value2

res=ss.post(url,headers=headers,data=data)

# print(res.text)
