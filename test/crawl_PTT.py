
import requests 
from bs4 import BeautifulSoup

import pandas as pd

board_name = "Gossiping"

url = 'https://www.ptt.cc/bbs/' + board_name + '/index.html'

response = requests.get(url, cookies={'over18': '1'})
soup = BeautifulSoup(response.text, "lxml")


df = {
    '日期':[],
    '作者':[],
    '標題':[],
    '看板名稱':[]
#     '內文':[]
    
}
pre_site = "www.ptt.cc"


for i in range(len(soup.find_all('div',class_="author"))):

  df['看板名稱'].append(soup.find_all('a',class_="board")[0].text[3:])
  df['作者'].append(soup.find_all('div',class_="author")[i].text)
  df['日期'].append(soup.find_all('div',class_="date")[i].text)
  df['標題'].append(soup.find_all('div',class_="title")[i].text[2:-1])
  
  
  
#   content_url = "http://www.ptt.cc" + soup.find_all('div',class_="r-ent")[i].find("a")['href']
#   response = requests.get(content_url, cookies={'over18': '1'})
#   soup = BeautifulSoup(response.text, "lxml")
  
#   df['標題'].append(soup.find_all('div',class_="bbs-screen bbs-content")) # [1].text 
  
  

  
pd.DataFrame(df)