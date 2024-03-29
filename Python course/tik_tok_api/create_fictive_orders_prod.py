
import requests
import json
from pprint import *


def fetch_user_posts():
    url = "https://tiktok-unauthorized-api-scraper-no-watermark-analytics-feed.p.rapidapi.com/api/search"
    body = {"username": "simba.tv2",
            "amount_of_posts": 10}

    headers = {'content-type': 'application/json',
               'X-RapidAPI-Key': 'fd80dfa220msha1c05eac4a74483p10c016jsn711bd34e755a',
               'X-RapidAPI-Host': 'tiktok-unauthorized-api-scraper-no-watermark-analytics-feed.p.rapidapi.com'}

    response = requests.post(url, headers=headers, json=body)
    return response


data = fetch_user_posts().json()
# pprint(data)

aweme_list = []


def fetch_posts_aweme_id(data):
    for key, value in data.items():
        if key == 'posts':
            for content in value:
                for aweme, aweme_value in content.items():
                    if aweme == 'aweme_id':
                        aweme_list.append(aweme_value)


def create_fictive_order(aweme):
    url = "https://fantik.linuxtech.io:8100/api/v1/orders/fictive/create"

    body = {"actionTypeId": 1,
            "awemeId": aweme,
            "shortLink": "",
            "actionsAmount": 500,
            "orderDurationHours": 12,
            "orderName": "fictive",
            "rewardId": None}

    response = requests.post(url, json=body)
    return print(f'Status code: {response.status_code}')


def create_multiple_fictive_orders():
    for aweme in aweme_list:
        create_fictive_order(aweme)


fetch_posts_aweme_id(data)
create_multiple_fictive_orders()

