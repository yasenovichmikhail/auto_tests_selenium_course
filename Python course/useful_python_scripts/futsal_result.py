import requests
from bs4 import BeautifulSoup
from Config import *
import schedule

SCORE = '0 : 0'
STATUS_MATCH_BEFORE = 'Матч еще не начинался'
STATUS_MATCH_END = 'Матч завершен'
HALF_TIME = 'Перерыв'


def get_content():
    url = "https://fc-stalitsa.by/live"
    headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 '
                             '(KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36'}

    page = requests.get(url=url, headers=headers)
    page.encoding = page.apparent_encoding
    return BeautifulSoup(page.text, 'html.parser')


def get_results(data):
    global SCORE
    global STATUS_MATCH_BEFORE
    all_headers = data.findAll('div', class_='match-live-container')
    for header in all_headers:
        status_online = header.find('div', class_='live-match-link').text.strip()
        if status_online != STATUS_MATCH_BEFORE or status_online != STATUS_MATCH_END or status_online != HALF_TIME:
            score = header.find('div', class_='live-match-result').text.strip()
            if score != SCORE:
                team1, team2 = header.findAll('span', class_='live-match-team-name')
                team1 = team1.text.strip().title()
                team2 = team2.text.strip().title()
                date_time = header.find('div', class_='st-vcenter live-match-result-content').text.strip()
                date_time = date_time.split('.')
                date = str(date_time[0])
                time = (date_time[1])
                text_message = f'{date}. {time}, {team1} {score} {team2}'
                print(text_message)
                send_msg(text_message)
                SCORE = score
            continue
        continue


def send_msg(text):
    token = TG_TOKEN
    chat_id = TG_CHAT_ID
    url_req = "https://api.telegram.org/bot" + token + "/sendMessage" + "?chat_id=" + chat_id + "&text=" + text
    results = requests.get(url_req)
    print(results.json())


def main():
    get_results(get_content())


if __name__ == '__main__':
    schedule.every(3).minutes.do(main)
    while True:
        schedule.run_pending()
