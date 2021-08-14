import requests
import json
from urllib import request
import os

if not os.path.exists('D:\python_code\pythonTestProject\dcardphoto\ '):
    os.mkdir("D:\python_code\pythonTestProject\dcardphoto\ ")

url= 'https://www.dcard.tw/service/api/v2/forums/photography/posts?limit=30&before=236646571'

userAgent='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36'
headers= {
    'User-Agent' : userAgent
}

res = requests.get(url,headers=headers)

# print(res.text)
jsondata = json.loads(res.text)

for articalDict in jsondata:
#     for key,value in r.items():
        # print(key ,":" , value)
        articalUrl='https://www.dcard.tw/f/photography/p/' + str(articalDict['id'])
        title=articalDict['title']
        print(articalUrl)
        for imgs in articalDict['mediaMeta']:
            print('\t' + imgs['url'])
            #imagepath = 'D:\python_code\pythonTestProject\dcardphoto\{}.{}'.format(title,imgs['url'].split('.')[-1])
            imagepath = 'D:\python_code\pythonTestProject\dcardphoto\{}_{}'.format(title, imgs['url'].split('/')[-1])
            #request.urlretrieve(imgs['url'],imagepath)
            imgContent=requests.get(imgs['url'],headers=headers).content
            with open(imagepath,'wb') as f:
                f.write(imgContent)
        print('=============')

# for i in jsondata[1]['mediaMeta']:
#     print(i['url'])