from urllib import request
import requests
from bs4 import BeautifulSoup
import os

if not os.path.exists('F:\python_code\pyETLProject\pttMovie\ ') :
    os.mkdir('F:\python_code\pyETLProject\pttMovie\ ')

url='https://www.ptt.cc/bbs/movie/index.html'



userAgent='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36'
headers= {
    'User-Agent' : userAgent
}

#req = request.Request(url=url,headers=headers)

#res = request.urlopen(req)



#html=res.read().decode('UTF-8')





#print(soup)

# logo = soup.select('a',{'id':'logo'})
# logo = soup.select('a',id='logo')
# print(logo[0].text)
# print(logo[0]['href'])
#
# content = soup.select('div',class_='bbs-content')
# print(len(content))

#board = content[0].findAll('a',class_='board')
#print(board)




for i in range(0,1):

    res = requests.get(url, headers=headers)

    html = res.text

    soup = BeautifulSoup(html, 'html.parser')

    titles = soup.select('div[class="title"]')

    for titleSoup in titles:
        try:
            title = titleSoup.select('a')[0].text
            articalUrl = "https://www.ptt.cc/" + titleSoup.select('a')[0]['href']
            #get artical content
            resArtical = requests.get(articalUrl, headers=headers)
            print(title)
            soupArticle = BeautifulSoup(resArtical.text, 'html.parser')
            #remove tag content
            articleContent = soupArticle.select('div[id="main-content"]')[0]
            for i in articleContent.select('div'):
                i.extract()
            for i in articleContent.select('span'):
                i.extract()

            articleContent =articleContent.text
            #print(articleContent)


            #normal content
            #articleContent = soupArticle.select('div[id="main-content"]')[0].text.split('※ 發信站:')[0]

            #write in file
            title=title.replace('/','-')
            title = title.replace('?', '')
            title = title.replace(':', '-')
            try:
                with open('F:\python_code\pyETLProject\pttMovie\{}.txt'.format(title),'w',encoding='utf-8') as f:
                    f.write(articleContent)
                    f.close
            except OSError:
                pass

        except IndexError:
            print(titleSoup)
        print('==========')

    newUrl='https://www.ptt.cc/' + soup.select('a[class="btn wide"]')[1]['href']
    url= newUrl