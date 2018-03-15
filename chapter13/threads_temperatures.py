from threading import Thread
import json
from urllib.request import urlopen
import time

CITIES = [
    'Edmonton', 'Victoria', 'Winnipeg', 'Fredericton',
    "St. John's", 'Halifax', 'Toronto', 'Charlottetown',
    'Quebec City', 'Regina'
]

class TempGetter(Thread):
    def __init__(self, city):
        super().__init__()
        self.city = city

    def run(self):
        url_template = (
            'http://api.openweathermap.org/data/2.5/weather'
            '?q={}&APPID=039b52688b0e58330ebdbd55e45c27ba')
        response = urlopen(url_template.format(self.city))
        data = json.loads(response.read())
        self.temperature = data['main']['temp']

