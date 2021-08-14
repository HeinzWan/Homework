from urllib import request

url='https://www.ptt.cc/bbs/joke/index.html'



userAgent='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36'
headers= {
    'User-Agent' : userAgent
}

req = request.Request(url=url,headers=headers)

res = request.urlopen(req)

html=res.read().decode('UTF-8')

print(html)