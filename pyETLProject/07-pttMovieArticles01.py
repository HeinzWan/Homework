from urllib import request
import requests
from bs4 import BeautifulSoup

url='https://www.ptt.cc/bbs/joke/index.html'



userAgent='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36'
headers= {
    'User-Agent' : userAgent
}

articalUrl= "https://www.ptt.cc/bbs/movie/M.1628251622.A.0D8.html"
resArtical =requests.get(articalUrl, headers=headers)

soupArticle = BeautifulSoup(resArtical.text,'html.parser')
# print(soupArticle.text)
articleContent = soupArticle.select('div[id="main-content"]')[0].text.split('※ 發信站:')[0]

print(articleContent)