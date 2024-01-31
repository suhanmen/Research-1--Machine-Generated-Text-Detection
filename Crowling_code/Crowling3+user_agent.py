import requests
from bs4 import BeautifulSoup
import os
import glob
from user_agent import generate_user_agent, generate_navigator
import random



def read_all_text_files(directory):
    # 주어진 디렉토리에서 모든 .txt 파일 찾기
    txt_files = glob.glob(os.path.join(directory, '*.txt'))
    #txt_files = [f for f in os.listdir(directory) if f.endswith('.txt')]

    if not txt_files:
        print(f"No .txt files found in the directory: {directory}")
        return
    
    content_list = []
    for txt_file in txt_files:
        # 각 .txt 파일 열어서 내용 출력
        with open(txt_file, 'r', encoding='utf-8') as file:
            content = file.read()
            content_list.append(content)

    return content_list

def find_data(site):
    total_list = []



    if not site:
        print("경로가 없음")
        print(site)
        # 비어있는 site는 건너뜁니다.
        return total_list
   
    else : 
        # url주소
        url = site
        print(site)
        #response = requests.get(url)
        total_list.append(site)

        # 추가부분###################
        hdr = {'User-Agent' : generate_user_agent(os='win', device_type='desktop')}
        response = requests.get(url = site, headers=hdr)
        content = BeautifulSoup(response.text, "html.parser")

       
        
        if response.status_code == 200:
            html = response.text
            soup = BeautifulSoup(html, 'html.parser')

            # 부모
            ul = soup.select_one('#repo-content-pjax-container > div > div > div.Layout.Layout--flowRow-until-md.react-repos-overview-margin.Layout--sidebarPosition-end.Layout--sidebarPosition-flowRow-end > div.Layout-sidebar > div > div:nth-child(1) > div')
            
            if ul:
                # 자식  Star, Forks
                count = ul.select('div > div > a > strong')
                for title in count[::2]:
                    total_list.append(title.get_text())


            # 자식 licese
                license = ul.select_one('div > div')
                li = license.get_text().split()
                if "License" in li:
                    index = li.index("License")+1
                    total_list.append(li[index])
                else:
                    total_list.append("None")
                print(total_list)
                return total_list
            

            else:
                print("No matching element found.")


        else : 
            print('wrong')
            print(response.status_code)
            print(site)
            total_list.append("x")
            return total_list

def save_results_to_txt(txt_list, output_directory, point):
    output_file_path = os.path.join(output_directory, f'result_{point + 243}.txt')
    with open(output_file_path, 'w', encoding='utf-8') as output_file:
        output_file.write('\n'.join(map(str, txt_list)))
    print(f"Result for file {point + 243} saved to {output_file_path}")


## 실행
directory_path = r'C:\Users\SJK\Desktop\ToC-Work\1.research(1)\Task1\Crowling\extracted_files\1.task_total_url'
output_directory = r'C:\Users\SJK\Desktop\ToC-Work\1.research(1)\Task1\Crowling\extracted_files\sample_results\2.agent'


site_list = []
site_count = []
site_list = read_all_text_files(directory_path)

point = 0


for i in site_list:
    txt_list = []
    site = i.split("\n")
    for path in site:
        result = find_data(path)
        txt_list.append(result)

    #print(txt_list)
    point += 1
    save_results_to_txt(txt_list, output_directory, point)