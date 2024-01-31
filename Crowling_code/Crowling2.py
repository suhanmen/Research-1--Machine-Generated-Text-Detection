import requests
from bs4 import BeautifulSoup



def find_url(site):
    # url주소
    url = 'https://github.com/hasnainnaeem/Violence-Detection-in-Videos'
    response = requests.get(url)
    total_list = []

    if response.status_code == 200:
        html = response.text
        soup = BeautifulSoup(html, 'html.parser')

        # 부모
        ul = soup.select_one('#repo-content-pjax-container > div > div > div.Layout.Layout--flowRow-until-md.react-repos-overview-margin.Layout--sidebarPosition-end.Layout--sidebarPosition-flowRow-end > div.Layout-sidebar > div > div:nth-child(1) > div')



        # 자식  Star, Forks
        count = ul.select('div > div > a > strong')
        for title in count[::2]:
            total_list.append(title.get_text())
            
        #print(total_list)



        # 자식 licese
        license = ul.select_one('div > div')
        print(license)
        li = license.get_text().split()
        print(li)
        if "License" in li:
            index = li.index("License")+1
            total_list.append(li[index])
        else:
            #print("None")
            total_list.append("None")

        print(total_list)

        

    else : 
        print(response.status_code)

find_url(0)