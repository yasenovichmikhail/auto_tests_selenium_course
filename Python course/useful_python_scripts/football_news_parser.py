from bs4 import BeautifulSoup
import requests
from config.config import *
import pandas as pd


def get_page_content(page):
    url = 'https://football.by/news/category/futbol-belarusi'
    headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 '
                             '(KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36'}
    params = {'page': page}

    page = requests.get(url, headers=headers, params=params)

    return BeautifulSoup(page.text, "html.parser")


def get_news(data):
    my_list = []
    all_headers = data.findAll('div', class_="card mx-0 col-lg-12 border-0 mb-2 px-0 pt-2")
    for header in all_headers:
        articles = {
            'Header': header.find('h3', class_='home_header mb-2 blue_hov').text,
            'Category': header.find('p', class_="new_type text-end").text,
            'Date': header.find('p', class_='new_date col-lg-12 mb-2').text,
            'Description': header.find('p', class_='new_tab_type_1_info blue_hov').text.strip()
        }
        my_list.append(articles)
    for news in my_list:
        print(news)


def main(page):
    get_news(get_page_content(page=page))


if __name__ == '__main__':
    main(1)

