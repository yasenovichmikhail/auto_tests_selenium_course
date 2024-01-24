import requests


url_api = 'https://api.midway.tomtom.com/ranking/liveHourly/USA_los-angeles'

usa_req = requests.get(url_api)

usa_json = usa_req.json()


# Do something with the json response to prove it works. 

print(usa_json)