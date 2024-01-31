import requests
from bs4 import BeautifulSoup

# url주소
url = 'https://github.com/marcochiesa/dicom-storescp'
response = requests.get(url)

if response.status_code == 200:
    html = response.text
    soup = BeautifulSoup(html, 'html.parser')

    # 부모
    div_container = soup.find('div', class_='js-social-container')  # 해당 div를 찾습니다.
    
    if div_container:
        star_count = div_container.find('a', class_='social-count')  # 클래스 이름이 social-count인 a 태그를 찾습니다.
        
        if star_count:
            print("Star Count:", star_count.text.strip())  # 필요에 따라 문자열의 공백을 제거할 수 있습니다.
        else:
            print("Star count element not found on the page.")
    else:
        print("Social container div not found on the page.")

else:
    print(response.status_code)
