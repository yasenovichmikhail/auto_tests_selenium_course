from bs4 import BeautifulSoup
import requests
import pandas as pd

url = 'https://football.by/news/category/futbol-belarusi'

page = requests.get(url)

soup = BeautifulSoup(page.text, "html.parser")

my_list = []

allHeaders = soup.findAll('div', class_='card-body')
for header in allHeaders:
    news = {
        'Data': header.find('p', class_='new_date').text,
        'Category': header.find('p', class_='new_type').text,
        'Title': header.find('h3', class_='home_header').text,
        'Description': header.find('p', class_='new_tab_type_1_info').text.strip()
    }
    my_list.append(news)

for action in my_list:
    print(action)
    
