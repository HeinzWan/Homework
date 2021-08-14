from urllib import request
import requests
from bs4 import BeautifulSoup

url='https://www.ptt.cc/bbs/joke/index.html'



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


for i in range(0,5):

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

            soupArticle = BeautifulSoup(resArtical.text, 'html.parser')
            articleContent = soupArticle.select('div[id="main-content"]')[0].text.split('※ 發信站:')[0]
            print(articleContent)
        except IndexError:
            print(titleSoup)
        print('==========')

    newUrl='https://www.ptt.cc/' + soup.select('a[class="btn wide"]')[1]['href']
    url= newUrl