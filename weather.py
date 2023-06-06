import requests

places = ['Лондон', 'Шереметьево', 'Череповец']

for place in places:
    url = f'https://wttr.in/{place}?nmMTq&lang=ru'
    response = requests.get(url)
    print(response.text)
