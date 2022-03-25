import requests
from bs4 import BeautifulSoup
url = 'http://ncov.mohw.go.kr/'

hf = requests.get(url)


if hf.status_code == 200:
        html = hf.text
        soup = BeautifulSoup(html, 'html.parser')
        count_corona = soup.select_one('#content > div > div>div.liveboard_layout > div.liveToggleOuter > div > div.live_left>div.occurrenceStatus > div.occur_graph > table > tbody > tr:nth-child(1) > td:nth-child(5) > span')
        print("오늘 코로나 확진자 :"+count_corona.get_text())
    
    
else :
        print(hf.status_code)