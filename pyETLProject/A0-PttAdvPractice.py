import requests
import traceback
from bs4 import BeautifulSoup
import os

if not os.path.exists('F:\python_code\pyETLProject\pttGossip\ ') :
    os.mkdir('F:\python_code\pyETLProject\pttGossip\ ')

resLandingPageUrl='https://www.ptt.cc/ask/over18?from=%2Fbbs%2FGossiping%2Findex.html'
askOver18Url = 'https://www.ptt.cc/ask/over18'
pttGossipUrl='https://www.ptt.cc/bbs/Gossiping/index.html'

userAgent='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36'
headers= {
    'User-Agent' : userAgent
}
ss = requests.session()

#進入首頁，會回傳確認over18頁面
resLandingPage = ss.get(resLandingPageUrl,headers=headers)
soupLandingPage = BeautifulSoup(resLandingPage.text,'html.parser')
#print(ss.cookies)

#將over18頁面上的內容提取
data=dict()
key1=soupLandingPage.select('input')[0]['name']
value1=soupLandingPage.select('input')[0]['value']
data[key1] =value1

key1=soupLandingPage.select('button')[0]['name']
value1=soupLandingPage.select('button')[0]['value']
data[key1] =value1
#進行submit over18頁面，之後cookie就會產生
ss.post(askOver18Url,headers=headers,data=data)
#print(ss.cookies)



def removeTag(content,*args):
    if(len(args) == 0):
        for i in content:
            i.extract()
    else:
        for i in content.select(args[0]):
            i.extract()


#可以開始進行網頁爬蟲
#只抓一頁
for i in range(0,1):
    #抓首頁
    res = ss.get(pttGossipUrl,headers=headers)

    html = res.text

    soup = BeautifulSoup(html, 'html.parser')
    #取得所有title
    titles = soup.select('div[class="r-ent"]')

    for titleSoup in titles:
        try:
            #推噓數
            nrecs = titleSoup.select('div[class="nrec"]')
            #清理tag
            # removeTag(nrecs)
            # for i in nrecs:
            #     i.extract()
            nrec = nrecs[0].text

            #作者
            authors = titleSoup.select('div[class="author"]')
            author = authors[0].text

            title = titleSoup.select('div[class="title"]')[0].select('a')[0].text

            #取得title的url
            articalUrl = "https://www.ptt.cc/" + titleSoup.select('a')[0]['href']
            #取得 文章內容artical content
            resArtical = ss.get(articalUrl, headers=headers)

            soupArticle = BeautifulSoup(resArtical.text, 'html.parser')

            #remove tag content
            articleContent = soupArticle.select('div[id="main-content"]')[0]

            removeTag(articleContent, 'div')
            removeTag(articleContent, 'span')

            articleContent =articleContent.text

            #date
            soupArticle = BeautifulSoup(resArtical.text, 'html.parser')
            date = soupArticle.select('span[class="article-meta-value"]')[3]

            date = date.text

            #normal content
            #articleContent = soupArticle.select('div[id="main-content"]')[0].text.split('※ 發信站:')[0]

            #write in file
            title=title.replace('/','-')
            title = title.replace('?', '')
            title = title.replace(':', '-')
            try:
                with open('F:\python_code\pyETLProject\pttGossip\{}.txt'.format(title),'w',encoding='utf-8') as f:
                    f.write("作者:"+author+"\n")
                    f.write("推噓數："+nrec+"\n")
                    f.write("時間:"+date+"\n")
                    f.write(articleContent)
                    f.close
            except OSError:
                pass

        except IndexError as e:
            traceback.print_exc()
        print('==========')

    newUrl='https://www.ptt.cc/' + soup.select('a[class="btn wide"]')[1]['href']
    url= newUrl

