import requests
import json
from bs4 import BeautifulSoup


url ='https://buzzorange.com/techorange/wp/wp-admin/admin-ajax.php'

userAgent='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36'
headers= {
    'User-Agent' : userAgent
}

datastr='''action: ceris_posts_listing_grid_b_no_sidebar
args[post_type]: post
args[ignore_sticky_posts]: 1
args[post_status]: publish
args[posts_per_page]: 6
args[offset]: 0
args[orderby]: date
postOffset: 12
type: loadmore
moduleInfo[post_source]: all
moduleInfo[post_icon]: disable
moduleInfo[iconPosition]: top-right
moduleInfo[post_icon_animation]: disable
moduleInfo[bookmark]: off
securityCheck: ab248723a6'''

data ={r.split(': ')[0]:r.split(': ')[1] for r in datastr.split('\n')}


for p in range(0,3):
    res = requests.post(url, headers=headers, data=data)
    # print(res.text)

    jsonData = json.loads(res.text)
    print(jsonData)
    soup = BeautifulSoup(jsonData, 'html.parser')
    titles = soup.select('h3[class="post__title typescale-2"] a')
    for title in titles:
        titleName = title.text
        articalUrl = title['href']
        print(titleName)
        print(articalUrl)
        print('=======')
    print('+++++++++++++++++++++')
    data['postOffset'] = str(int(data['postOffset'])+6)
