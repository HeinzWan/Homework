import requests
from bs4 import BeautifulSoup

url='https://www.ptt.cc/bbs/Gossiping/index.html'


userAgent='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36'
headers= {
    'User-Agent' : userAgent
}
cookies ={
    'over18' : '1'
}

res = requests.get(url,headers=headers,cookies=cookies)

print(res.text)