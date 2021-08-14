from urllib import request
from bs4 import BeautifulSoup

url='https://www.ptt.cc/bbs/joke/index.html'



userAgent='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36'
headers= {
    'User-Agent' : userAgent
}

req = request.Request(url=url,headers=headers)

res = request.urlopen(req)

html=res.read().decode('UTF-8')

soup = BeautifulSoup(html,'html.parser')

print(soup)

logo = soup.findAll('a',{'id':'logo'})
logo = soup.findAll('a',id='logo')
print(logo[0].text)
print(logo[0]['href'])

content = soup.findAll('div',class_='bbs-content')
#print(content)