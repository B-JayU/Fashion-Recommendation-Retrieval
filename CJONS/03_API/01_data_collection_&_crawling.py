# -*- coding: utf-8 -*-

### impotring

from bs4 import BeautifulSoup as bs
from urllib.request import urlopen, Request, urlretrieve
from urllib.request import Request
from urllib.parse import quote_plus
from PIL import Image

style_group = ['americancasual', 'casual', 'dandy', 'formal', 'sports', 'street']

baseUrl01 = "https://www.musinsa.com/app/styles/lists?use_yn_360=&style_type="
baseUrl02 = "&brand=&model=&tag_no=&max_rt=&min_rt=&display_cnt=60&list_kind=big&sort=date&page="
page_num = 1

for g_id in range(len(style_group)):
    name_style = style_group[g_id]
    search_url = baseUrl01 + name_style + baseUrl02 + str(page_num)

    html = Request(search_url, headers={'User-Agent' : 'Mozilla/5.0'})
    page = urlopen(html)

    # print(page)

    soup = bs(page, "html.parser")
    img = soup.find_all(class_='style-list-thumbnail__img')

    folder_name = './' + name_style + '/'
    n = 1
    for i in img:
        # print(n)
        n += 1
        # print(i)
        imgUrl = 'https:' + i['src']

        image_name = name_style + '_' + str(n).zfill(3) + '.jpg'
        urlretrieve(imgUrl, folder_name + image_name)

        img = Image.open(folder_name + image_name)
        # print(img)
    
    print('Image Crawling is done.')