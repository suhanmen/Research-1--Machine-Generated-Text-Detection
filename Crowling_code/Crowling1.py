# star의 숫자값만 뽑아냄.

import requests
from bs4 import BeautifulSoup



# url주소
url = 'https://github.com/marcochiesa/dicom-storescp'


response = requests.get(url)

if response.status_code == 200:
    html = response.text
    soup = BeautifulSoup(html, 'html.parser')

    # 부모
    ul = soup.select_one('#repo-content-pjax-container > div > div > div.Layout.Layout--flowRow-until-md.react-repos-overview-margin.Layout--sidebarPosition-end.Layout--sidebarPosition-flowRow-end > div.Layout-sidebar > div > div:nth-child(1) > div > div') 
    titles = ul.select('li > dl > dt > a') # 자식
    print(titles)


    """
    #Star
    star_count = soup.select_one('#repo-content-pjax-container > div > div > div.Layout.Layout--flowRow-until-md.react-repos-overview-margin.Layout--sidebarPosition-end.Layout--sidebarPosition-flowRow-end > div.Layout-sidebar > div > div:nth-child(1) > div > div > div:nth-child(6) > a > strong') # 부모
    #Forks
    fork_count = soup.select_one('#repo-content-pjax-container > div > div > div.Layout.Layout--flowRow-until-md.react-repos-overview-margin.Layout--sidebarPosition-end.Layout--sidebarPosition-flowRow-end > div.Layout-sidebar > div > div:nth-child(1) > div > div > div:nth-child(10) > a > strong')
    #license
    license = soup.select_one('#repo-content-turbo-frame > div > div > div.Layout.Layout--flowRow-until-md.react-repos-overview-margin.Layout--sidebarPosition-end.Layout--sidebarPosition-flowRow-end > div.Layout-sidebar > div > div:nth-child(1) > div > div > div:nth-child(9) > a')
    
    
    if star_count and fork_count:
        print(star_count.get_text())
        print(fork_count.get_text())
    else:
        print("Problem")


    if license:
        print(license.get_text())
    else:
        print("None")
    """

else : 
    print(response.status_code)

    