import requests
from bs4 import BeautifulSoup


def get_content(go_from, go_to, date):
    url = f"https://poezdato.net/raspisanie-poezdov/{go_from}--{go_to}/elektrichki/{date}/"
    headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 '
                             '(KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36'}

    page = requests.get(url=url, headers=headers)
    return BeautifulSoup(page.text, 'html.parser')


def get_schedule(data):
    all_headers = data.findAll('tr')
    for header in all_headers[1:]:
        date1, date2 = header.findAll('span', class_='_time')
        print(f'Отправление {date1.text}, прибытие {date2.text}')


get_schedule(get_content('borisov', 'minsk', '29.08.2024'))
